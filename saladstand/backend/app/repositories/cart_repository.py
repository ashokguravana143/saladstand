from sqlalchemy.orm import Session
from app.models.cart import Cart

def add_to_cart(db: Session, user_id: int, menu_id: int, quantity: int):
    
    existing = db.query(Cart).filter(
        Cart.user_id == user_id,
        Cart.menu_id == menu_id
    ).first()

    if existing:
        existing.quantity += quantity
    else:
        new_item = Cart(user_id=user_id, menu_id=menu_id, quantity=quantity)
        db.add(new_item)

    db.commit()


def get_cart_items(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).all()


def remove_item(db: Session, user_id: int, menu_id: int):
    item = db.query(Cart).filter(
        Cart.user_id == user_id,
        Cart.menu_id == menu_id
    ).first()

    if item:
        db.delete(item)
        db.commit()

def clear_cart(db, user_id):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()

    for item in cart_items:
        db.delete(item)

    db.commit()