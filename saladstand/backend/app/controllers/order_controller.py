from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.services.order_service import place_order, update_order_status
from app.schemas.order_schema import OrderCreate
from app.core.dependencies import get_current_user
from app.models.order import OrderStatus
router = APIRouter(prefix="/orders")

@router.post("/place")
def place_order_api(order: OrderCreate, db=Depends(get_db), user=Depends(get_current_user)):
    
    order_obj = place_order(db, user["user_id"], order.payment_method)

    return {
        "id": order_obj.id,
        "status": order_obj.status,
        "total_amount": order_obj.total_amount
    }

@router.put("/status/{order_id}")
def update_status(
    order_id: int,
    status: OrderStatus,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    order = update_order_status(db, order_id, status, user)

    return {
        "id": order.id,
        "status": order.status
    }