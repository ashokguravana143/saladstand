from sqlalchemy import Column, Integer, Boolean
from app.db.database import Base

class SystemConfig(Base):
    __tablename__ = "system_config"

    id = Column(Integer, primary_key=True)
    cod_enabled = Column(Boolean, default=True)