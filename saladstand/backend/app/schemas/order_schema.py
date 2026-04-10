from pydantic import BaseModel

class OrderCreate(BaseModel):
    payment_method: str  # COD / ONLINE

class OrderResponse(BaseModel):
    id: int
    status: str
    total_amount: int

    class Config:
        from_attributes = True