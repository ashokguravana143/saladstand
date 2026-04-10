from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role")

    # Customer orders
orders = relationship("Order", foreign_keys="Order.user_id", back_populates="user")

# Delivery assigned orders
deliveries = relationship("Order", foreign_keys="Order.delivery_boy_id", back_populates="delivery_boy")