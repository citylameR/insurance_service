from tortoise.models import Model
from tortoise import fields


class InsuranceRate(Model):
    id = fields.IntField(pk=True)
    date = fields.CharField(max_length=10)
    cargo_type = fields.CharField(max_length=50)
    rate = fields.FloatField()
