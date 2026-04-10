from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import menu_service
from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.menu_schema import MenuCreate, MenuResponse
router = APIRouter(prefix="/menu", tags=["Menu"])

# ✅ Admin adds menu
@router.post("/")
def create_menu(
    menu: MenuCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["role"] != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin access required")

    return menu_service.add_menu(db, menu)


# ✅ Customer views menu
@router.get("/", response_model=list[MenuResponse])
def get_menus(db: Session = Depends(get_db)):
    return menu_service.list_menus(db)