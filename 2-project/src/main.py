from fastapi import FastAPI, HTTPException
from src.models import Product
from src.schemas import ApiResponse

app = FastAPI()


# test api
@app.get("/")
def home():
    return "Homepage"


products = [
    Product(id=1, name="Phone", description="Budget Phone", price=499.9, quantity=100),
    Product(id=2, name="Laptop", description="Gaming Laptop", price=999.9, quantity=35),
    Product(id=3, name="Laptop", description="Gaming Laptop", price=999.9, quantity=35),
]


# return all products
@app.get("/products")
def get_all_products():
    return products


# return a specific product by id
# {id}: a variable/placeholder to catch the passed argument in query /product/1
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for p in products:
        if p.id == id:
            return p

    raise HTTPException(status_code=404, detail="Product not found")


# add a product
@app.post("/product")
def add_product(product: Product):
    products.append(product)

    # return simple message
    # return "Product added successfully!"

    # return python standard dict
    # return {"status": 200, "message": "Product saved successfully!", "data": product}

    # use pydantic so fastapi automatically converts pydantic attr's to json
    return ApiResponse(status=200, message="Product saved successfully!", data=product)
