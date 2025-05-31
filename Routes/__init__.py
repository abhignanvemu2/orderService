from fastapi import APIRouter
from .Order import router as Order

router = APIRouter()

router.include_router(Order, prefix="/order", tags=['order'])