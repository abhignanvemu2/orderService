from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Models.OrderModel import Order
from Config import get_db
from Schemas.Order import StatusUpdate
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.patch('/{orderId}/status')
def pending_order(orderId: int, data: StatusUpdate, db: Session = Depends(get_db)):
    try:
        order = db.get(Order, orderId)

        if order is None:
            raise HTTPException(status_code=404, detail="No orders found")
        
        order.status = data.status

        db.commit()
        db.refresh(order)

        return order
    
    except SQLAlchemyError as e:
        
        db.rollback() 
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    except Exception as e:
        
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
