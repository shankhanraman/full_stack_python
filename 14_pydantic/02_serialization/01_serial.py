# Serialzition is converting pydantic ddata models into python dcit JSON or XML format
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str    

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime = datetime.now()
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders = { datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="John Doe",
    email="abc@gmail.com",
    created_at=datetime(2023,10,1,10,30),
    address=Address(
        street="123 Main St",
        city="New York",
        postal_code="10001"
    ),
    is_active=False,
    tags=["premimum","subscriber"]
)

python_dict = user.model_dump()  # Convert to dictionary
print("Python Dict:", python_dict)
print(user)
json_str = user.model_dump_json()  # Convert to JSON string
print("JSON String:", json_str)    