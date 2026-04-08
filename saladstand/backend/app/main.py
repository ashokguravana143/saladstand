from fastapi import FastAPI
from app.db.database import engine, Base
import app.models  # IMPORTANT

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "SaladStand API Running 🚀"}