from fastapi import FastAPI
from src.models import Product

# instantiate FastAPI
app = FastAPI(
    title="First Project",
    description="First Project",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# products list
products = [
    Product(id=1, name="Phone", description="Budget Phone", price=499.9, quantity=100),
    Product(id=2, name="Laptop", description="Gaming Laptop", price=999.9, quantity=35),
]


# test route
@app.get("/")
def home():
    return "homepage"


# return products
@app.get("/products")
async def get_all_products():
    return products
