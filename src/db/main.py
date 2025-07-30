# Note : We are using asyncpg(Database), so we need to create Async Engine

from sqlmodel import create_engine,text,SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine,create_async_engine
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker


async_engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    echo=True
))

# App Starting Function
async def init_db():
    async with async_engine.begin() as conn:
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print(result.all())

        from src.books.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    Session =  async_sessionmaker(
        bind = async_engine,
        class_= AsyncSession,
        expire_on_commit=False   # Not Close Session after commiting to transaction
    )

    async with Session() as session:
        yield session
    


