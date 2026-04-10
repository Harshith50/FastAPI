from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from src.config import config


engine = create_async_engine(
    config.DATABASE_URL,
    echo=True,
)

async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")

        result = await conn.execute(statement) 

        print(result.all())   