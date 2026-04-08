from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    is_available = Column(Boolean, default=True)