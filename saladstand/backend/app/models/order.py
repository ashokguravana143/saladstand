import enum
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Enum, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base 

class OrderStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    READY_TO_PICK = "READY_TO_PICK"
    PICKED_UP = "PICKED_UP"
    DELIVERED = "DELIVERED"  

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Float)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    payment_method = Column(String)
    delivery_boy_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    delivered_at = Column(DateTime, nullable=True)

    # ✅ Customer
    user = relationship("User", foreign_keys=[user_id])

    # ✅ Delivery Boy
    delivery_boy = relationship("User", foreign_keys=[delivery_boy_id])

    items = relationship("OrderItem", back_populates="order")

    user = relationship("User", foreign_keys=[user_id], back_populates="orders")
    delivery_boy = relationship("User", foreign_keys=[delivery_boy_id], back_populates="deliveries")
    
