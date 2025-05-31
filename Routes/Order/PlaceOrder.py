from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Models.OrderModel import Order
from Schemas.Order import CreateOrder
from Config import get_db
from Models.MenuItem import MenuItem
from Models.UserModel import User
from Models.RestaurentModel import Restaurant
# from Models.DeliveryAgent import DeliveryAgent

router = APIRouter()

@router.post('/place')
def place_order(data: CreateOrder, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == data.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        restaurant = db.query(Restaurant).filter(Restaurant.id == data.restaurent_id).first()
        if not restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")
        
        menu_item = db.query(MenuItem).filter(MenuItem.id == data.menu_item_id).first()
        if not menu_item:
            raise HTTPException(status_code=404, detail="Menu item not found")
        
        # Optional: Delivery agent selection
        # deliveryAgent = db.query(DeliveryAgent).filter(DeliveryAgent.is_available == 1).first()

        # if deliveryAgent is None:
        #     deliveryAgent = db.query(DeliveryAgent).first()

        # Proceed with creating the order if all fields are valid
        new_order = Order(
            user_id=data.user_id,
            restaurant_id=data.restaurent_id,
            status=0,  # pending
            delivery_status=0,  # not assigned
            item_id=data.menu_item_id,
            delivery_agent_id=None  # or use some valid agent ID
            # delivery_agent_id=deliveryAgent.id
        )

        db.add(new_order)
        db.commit()
        db.refresh(new_order)  # Ensure the instance is passed to refresh

        return new_order

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
