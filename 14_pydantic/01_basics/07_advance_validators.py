from pydantic import BaseModel, Field, field_validator , model_validator
from datetime import datetime
class Person(BaseModel):
    first_name: str
    last_name: str
# Multiple field validation 
    @field_validator('first_name', 'last_name')
    def names_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Names must be capitalized")
        return value

class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, value):
        return value.lower().strip()

class Product(BaseModel):
    price: str # $4.4 or $4,44

    @field_validator('price', mode='before')
    def parse_price(cls, value):
        if isinstance(value, str) and value.startswith('$'):
            return float(value.replace('$','').replace(',',''))
        raise ValueError("Price must be a string starting with '$'")

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values['end_date'] <= values['start_date']:
            raise ValueError("end_date must be after start_date")
        return values