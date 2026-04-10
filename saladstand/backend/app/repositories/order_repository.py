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