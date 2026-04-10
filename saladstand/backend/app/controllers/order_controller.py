from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from app.services.order_service import place_order, update_order_status
from app.schemas.order_schema import OrderCreate
from app.core.dependencies import get_current_user
from app.models.order import OrderStatus
from app.repositories.order_repository import get_delivered_orders_by_delivery, get_ready_orders
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

@router.get("/ready")
def get_ready_orders_api(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "DELIVERY":
        raise HTTPException(status_code=403, detail="Only delivery boys allowed")

    orders = get_ready_orders(db)

    return [
        {
            "id": o.id,
            "total_amount": o.total_amount,
            "status": o.status
        }
        for o in orders
    ]

@router.get("/delivery/earnings")
def delivery_earnings(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "DELIVERY":
        raise HTTPException(status_code=403, detail="Only delivery boys allowed")

    orders = get_delivered_orders_by_delivery(db, user["user_id"])

    result = []

    for o in orders:
        commission = o.total_amount * 0.2

        result.append({
            "order_id": o.id,
            "total": o.total_amount,
            "commission": commission
        })

    return result