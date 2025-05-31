from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Models.OrderModel import Order
from Models.DeliveryAgent import DeliveryAgent
from Config import get_db

router = APIRouter()

@router.get('/{orderId}&{deliveryPersonId}')
def AssignToDeliveyPerson(orderId: int, deliveryPersonId:int, db: Session = Depends(get_db)):
    try:
        # status == 1 => pending orders
        order = db.get(Order, orderId)
        deliveryPerson = db.get(DeliveryAgent, deliveryPersonId)
        if order is None :
            HTTPException(status_code=500, detail=f"No Order Found")
        deliveryPerson.is_available = 0
        order.delivery_agent_id = deliveryPersonId
        order.delivery_status = 1
        order.status = 1

        db.commit()
        db.refresh(order)
        return order

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
