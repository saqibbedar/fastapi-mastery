from sqlalchemy.ext.asyncio import AsyncSession
from src.models import ProductModel
from src.schemas import ProductSchema

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product(self, product: ProductSchema) -> ProductModel:
        # 1. convert pydantic validation object ot SQLAlchemy Database Model object 
        new_product = ProductModel(
            name= product.name,
            description=product.description,
            price=product.price,
            category=product.category,
            image_url=product.image_url
        )

        # 2. Add to transaction and commit
        self.db.add(new_product)
        await self.db.commit()

        # 3. Refresh to get the generated primary key (id) from psql
        await self.db.refresh(new_product)
        return new_product