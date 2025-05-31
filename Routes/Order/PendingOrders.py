from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Models.OrderModel import Order
from Config import get_db

router = APIRouter()

@router.get('/pending')
def pending_order(db: Session = Depends(get_db)):
    try:
        # status == 1 => pending orders
        pending_orders = db.query(Order).filter(Order.status == 0).all()

        if not pending_orders:
            raise HTTPException(status_code=404, detail="No pending orders found")

        return pending_orders

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
