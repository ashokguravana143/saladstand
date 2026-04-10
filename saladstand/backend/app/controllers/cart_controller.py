from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cart_schema import AddToCart
from app.services import cart_service
from app.db.database import get_db
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])

# ✅ Add to cart
@router.post("/")
def add_to_cart(
    data: AddToCart,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    cart_service.add_item(db, user["user_id"], data)
    return {"message": "Item added to cart"}


# ✅ View cart
@router.get("/")
def get_cart(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return cart_service.get_items(db, user["user_id"])


# ✅ Remove item
@router.delete("/{menu_id}")
def remove_item(
    menu_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    cart_service.delete_item(db, user["user_id"], menu_id)
    return {"message": "Item removed"}