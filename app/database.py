from sqlalchemy.ext.asyncio import (
    create_async_engine,async_sessionmaker
)
from sqlalchemy.orm import declarative_base

engine = create_async_engine(
        url=DATABASE_URL,
        echo=True
    )
async_session = async_sessionmaker(bind=engine,autoflush=False,expire_on_commit=False,class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session

