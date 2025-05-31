from fastapi import APIRouter
from .PlaceOrder import router as  PlaceOrder
from .PendingOrders import router as PendingOrders
from .updateStatus import router as UpdateStatus
from .AssignOrder import router as AssignDeliveryPerson

router = APIRouter()

router.include_router(PlaceOrder)
router.include_router(PendingOrders)
router.include_router(UpdateStatus)
router.include_router(AssignDeliveryPerson)
