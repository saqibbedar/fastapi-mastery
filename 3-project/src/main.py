# app entrypoint

from fastapi import FastAPI, HTTPException

from src.repositories import ProductRepository
from src.schemas import ApiResponse

# instantiate app
app = FastAPI()


# test api
@app.get("/")
def home():
    return ApiResponse(status_code=200, message="Welcome to homepage", data=None)


# instantiate ProductRepository
product = ProductRepository()


# =======================================================================================
#                           API Endpoints / Get Methods                                 #
# =======================================================================================


# all products
@app.get("/products")
def get_all_products():
    return ApiResponse(status_code=200, message="All products", data=product.get_all())


# pagination
@app.get("/products/search/page")
def get_product_by_pagination(q: str, skip: int = 0, limit: int = 10):
    filtered_products: dict | None = product.get_by_pagination(q=q, skip=skip, limit=limit)

    if filtered_products and filtered_products["total_matches"] > 0 and len(filtered_products["results"]) > 0:
        return ApiResponse(status_code=200, message="Paginated products", data=filtered_products)
    else:
        raise HTTPException(status_code=404, detail=f"No product matched with provided query: {q}")


# search a product
@app.get("/products/search")
def get_product_by_query(q: str):

    filtered_products: list | None = product.get_by_query(q=q)

    if filtered_products:
        if len(filtered_products) > 0:
            return ApiResponse(status_code=200, message="Matched products", data=filtered_products)
        else:
            raise HTTPException(status_code=404, detail=f"No product matched with provided query: {q}")


# product by id
@app.get("/products/{id}")
def get_product_by_id(id: int):

    p: dict | None = product.get_by_id(id=id)

    if p:
        return ApiResponse(status_code=200, message="Matched product", data=p)
    else:
        raise HTTPException(status_code=404, detail="Product not found")
