from app.models.order import Order
from app.models.order_item import OrderItem
from app.repositories.cart_repository import get_cart_items, clear_cart
from app.repositories.menu_repository import get_menu_by_id
from fastapi import HTTPException
from app.models.order import OrderStatus
from app.repositories.order_repository import get_order_by_id

def update_order_status(db, order_id, new_status, user):

    order = get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")  

    # 🔥 ADMIN FLOW
    if user["role"] == "ADMIN":

        if new_status == OrderStatus.ACCEPTED:
            if order.status != OrderStatus.PENDING:
                raise HTTPException(status_code=400, detail="Only PENDING orders can be accepted")

        elif new_status == OrderStatus.READY_TO_PICK:
            if order.status != OrderStatus.ACCEPTED:
                raise HTTPException(status_code=400, detail="Only ACCEPTED orders can be marked ready")

    # 🔥 DELIVERY FLOW
    elif user["role"] == "DELIVERY":

        if new_status == OrderStatus.PICKED_UP:
            if order.status != OrderStatus.READY_TO_PICK:
                raise HTTPException(status_code=400, detail="Order not ready for pickup")

        elif new_status == OrderStatus.DELIVERED:
            if order.status != OrderStatus.PICKED_UP:
                raise HTTPException(status_code=400, detail="Order not picked yet")

    else:
        raise HTTPException(status_code=403, detail="Unauthorized role")

    # ✅ Update
    order.status = new_status

    if new_status == OrderStatus.DELIVERED:
        from datetime import datetime
        order.delivered_at = datetime.utcnow()

    db.commit()
    db.refresh(order)

    return order


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