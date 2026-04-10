from pydantic import BaseModel

class MenuCreate(BaseModel):
    name: str
    description: str
    price: float

class MenuResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool

    class Config:
        from_attributes = True