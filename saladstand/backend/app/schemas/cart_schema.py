from pydantic import BaseModel

class AddToCart(BaseModel):
    menu_id: int
    quantity: int

class CartResponse(BaseModel):
    menu_id: int
    quantity: int

    class Config:
        from_attributes = True