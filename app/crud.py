from app.models import InsuranceRate


async def get_rate_by_date_and_cargo_type(date: str, cargo_type: str):
    return await InsuranceRate.filter(date=date, cargo_type=cargo_type).first()
