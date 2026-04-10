from app.models.order import Order
from app.models.order_item import OrderItem
from app.repositories.cart_repository import get_cart_items, clear_cart
from app.repositories.menu_repository import get_menu_by_id
from fastapi import HTTPException
def place_order(db, user_id, payment_method):

    cart_items = get_cart_items(db, user_id)

    if not cart_items:
        raise HTTPException(status_code=403, detail="Cart is empty")

    total = 0

    # Create order first
    order = Order(
        user_id=user_id,
        payment_method=payment_method,
        total_amount=0  # temp
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    # Add items
    for item in cart_items:
        menu = get_menu_by_id(db, item.menu_id)

        item_total = menu.price * item.quantity
        total += item_total

        order_item = OrderItem(
            order_id=order.id,
            menu_id=item.menu_id,
            quantity=item.quantity,
            price=menu.price   # 🔥 IMPORTANT
        )
        db.add(order_item)

    # Update total
    order.total_amount = total
    db.commit()

    # Clear cart
    clear_cart(db, user_id)

    return order