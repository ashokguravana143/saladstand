from fastapi import FastAPI
from app.db.database import engine, Base
import app.models  # IMPORTANT
from app.utils.seed import seed_roles
from app.controllers import auth_controller
from app.controllers import admin_controller
from app.controllers import menu_controller

app = FastAPI()
seed_roles()

Base.metadata.create_all(bind=engine)
app.include_router(auth_controller.router, prefix="/auth")
app.include_router(admin_controller.router, prefix="/admin")
app.include_router(menu_controller.router, prefix="/menu")
@app.get("/")
def home():
    return {"message": "SaladStand API Running 🚀"}