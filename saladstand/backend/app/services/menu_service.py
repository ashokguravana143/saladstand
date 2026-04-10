from app.repositories import menu_repository

def add_menu(db, menu_data):
    return menu_repository.create_menu(db, menu_data)

def list_menus(db):
    return menu_repository.get_all_menus(db)