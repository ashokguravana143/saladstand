from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.repositories.order_repository import get_admin_earnings

router = APIRouter(prefix="/admin")

@router.get("/dashboard")
def admin_dashboard(user=Depends(get_current_user)):
    
    if user["role"] != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin access required")

    return {"message": "admin API Running 🚀"}

@router.get("/earnings")
def admin_earnings(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")

    orders = get_admin_earnings(db)

    total = sum(o.total_amount for o in orders)

    return {
        "total_earnings": total,
        "orders_count": len(orders)
    }