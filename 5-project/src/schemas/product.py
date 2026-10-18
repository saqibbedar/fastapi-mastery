lazy from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    category: str
    image_url: str

# Schema for outgoing API response data (includes ID)
class ProductResponse(ProductSchema):
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy model attributes