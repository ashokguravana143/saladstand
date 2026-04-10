from app.repositories import cart_repository

def add_item(db, user_id, data):
    cart_repository.add_to_cart(db, user_id, data.menu_id, data.quantity)

def get_items(db, user_id):
    return cart_repository.get_cart_items(db, user_id)

def delete_item(db, user_id, menu_id):
    cart_repository.remove_item(db, user_id, menu_id)