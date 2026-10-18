lazy import os
lazy from dotenv import load_dotenv
lazy from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# 1. Load .env file
load_dotenv()
DATABASE_URL: str = str(os.getenv("DATABASE_URL"))

# 2. create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# 3. create a session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# 4. database session dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()