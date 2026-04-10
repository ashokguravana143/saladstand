from app.models.order import Order




def create_order(db, order):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def create_order_item(db, item):
    db.add(item)
    db.commit()

def get_order_by_id(db, order_id):
    return db.query(Order).filter(Order.id == order_id).first()

def get_ready_orders(db):
    from app.models.order import OrderStatus
    return db.query(Order).filter(Order.status == OrderStatus.READY_TO_PICK).all()

def get_delivered_orders_by_delivery(db, user_id):
    from app.models.order import OrderStatus
    return db.query(Order).filter(
        Order.status == OrderStatus.DELIVERED,
        Order.delivery_boy_id == user_id
    ).all()


from datetime import datetime, timedelta

def get_admin_earnings(db):
    from app.models.order import OrderStatus

    last_90_days = datetime.utcnow() - timedelta(days=90)

    return db.query(Order).filter(
        Order.status == OrderStatus.DELIVERED,
        Order.delivered_at >= last_90_days
    ).all()