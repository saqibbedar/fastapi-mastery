from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.core import get_db
from src.schemas import ProductSchema, ProductResponse
from src.repositories import ProductRepository


router = APIRouter()

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_new_product(product: ProductSchema, db: AsyncSession=Depends(get_db)):
    # Initialize the repository with the checkout session
    repo = ProductRepository(db)

    try:
        return await repo.create_product(product=product)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not create product: {str(e)}"
        )