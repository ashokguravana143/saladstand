from sqlalchemy.orm import Session
from app.models.menu import Menu

def create_menu(db: Session, menu_data):
    menu = Menu(**menu_data.dict())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu

def get_all_menus(db: Session):
    return db.query(Menu).filter(Menu.is_available == True).all()

def get_menu_by_id(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()

    if not menu:
        raise Exception("Menu item not found")

    return menu