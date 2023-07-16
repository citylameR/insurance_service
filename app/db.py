from tortoise import Tortoise

from app.main import PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_DB


async def init():
    await Tortoise.init(
        db_url=f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}",
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()


async def close():
    await Tortoise.close_connections()
