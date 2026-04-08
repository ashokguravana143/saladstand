from fastapi import FastAPI
from app.db.database import engine, Base
import app.models  # IMPORTANT
from app.utils.seed import seed_roles
from app.controllers import auth_controller


app = FastAPI()
seed_roles()

Base.metadata.create_all(bind=engine)
app.include_router(auth_controller.router, prefix="/auth")

@app.get("/")
def home():
    return {"message": "SaladStand API Running 🚀"}