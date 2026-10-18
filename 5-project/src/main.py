from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

# routers
from src.api.v1.endpoints import ProductRouter

# Import database from core
from src.core import Base, get_db, engine

# model 
from src.models import ProductModel

# Lifespan event to create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Dispose connection pool on shutdown
    await engine.dispose()

# instantiate fastapi
app = FastAPI(title="Project 5", lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "FastAPI app is running"}

@app.get("/test-db")
async def test_db(db: AsyncSession=Depends(get_db)):
    try:
        # run a simple query to verify connection works
        result = await db.execute(text("SELECT 1"))
        value = result.scalar()

        return {
            "status": "success",
            "message": "Database connected successfully!",
            "probe_result": value
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed: {str(e)}"
        )

# ================================
# Product endpoints
# ================================
app.include_router(ProductRouter, prefix="/api/v1/products", tags=["Products"])