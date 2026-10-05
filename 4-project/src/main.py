import json

from fastapi import FastAPI, HTTPException

from src.repositories import ProductRepository
from src.schemas import ApiResponse

# instantiate app
app = FastAPI()


# test-api
@app.get("/")
def home():
    return ApiResponse(status_code=200, message="Homepage", data=None)


# instantiate product repository
product = ProductRepository()


@app.get("/products")
def get_all_products():
    try:
        # read data
        payload: dict | None = product.get_all()

        # breakpoint() # debugging

        if payload:
            return ApiResponse(status_code=200, message="All products", data=product.get_all())

        raise HTTPException(status_code=404, detail="No product found")
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        print(e)
        raise HTTPException(status_code=400, detail="Internal server error")


@app.get("/products/search")
def search_product(q: str, skip: int = 0, limit: int = 10):
    try:
        payload: dict | None = product.search(q, skip, limit)

        if not payload:
            raise HTTPException(status_code=404, detail="No product found")

        return ApiResponse(status_code=200, message="Matched products", data=payload)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error: Database issue")


@app.get("/products/{id}")
def get_product_by_id(id: int):
    try:
        payload: dict | None = product.get_by_id(id=id)

        if payload:
            return ApiResponse(status_code=200, message="Matched product", data=payload)

        raise HTTPException(status_code=404, detail="Product not found")
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error: Database issue")
