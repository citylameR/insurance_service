from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise
import os

app = FastAPI()

PG_USER = os.getenv('PG_USER', 'app')
PG_PASSWORD = os.getenv('PG_PASSWORD', '1234')
PG_DB = os.getenv('PG_DB', 'app')
PG_HOST = os.getenv('PG_HOST', '127.0.0.1')
PG_PORT = os.getenv('PG_PORT', 5431)


class InsuranceRequest(BaseModel):
    cargo_type: str
    declared_value: float


class InsuranceRate(BaseModel):
    date: str
    cargo_type: str
    rate: float


def load_rates_from_json():
    rates = [
        {
            "date": "2020-06-01",
            "cargo_type": "Glass",
            "rate": 0.04
        },
        {
            "date": "2020-06-01",
            "cargo_type": "Other",
            "rate": 0.01
        },

    ]
    return rates


def calculate_insurance_cost(cargo_type: str, declared_value: float, rates: list):
    for rate in rates:
        if rate["cargo_type"] == cargo_type:
            return declared_value * rate["rate"]
    raise HTTPException(status_code=400, detail="Invalid cargo type")


@app.on_event("startup")
async def startup_event():
    global rates
    rates = load_rates_from_json()


# Роут для расчёта страховой стоимости
@app.post("/calculate_insurance/")
async def calculate_insurance(request: InsuranceRequest):
    return {"insurance_cost": calculate_insurance_cost(request.cargo_type, request.declared_value, rates)}


# Настройки для подключения к базе данных PostgreSQL
DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

# Настройки для Tortoise ORM
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models"],
            "default_connection": "default",
        }
    }
}

# Регистрация моделей и подключение к базе данных
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
