from typing import Optional 
from pydantic import BaseModel, Field
import re
class Employee(BaseModel):
    id : int
    name: str = Field(
        ..., # Required field
        min_length=3, 
        max_length=50,
        description="Employee Name",
        example="Hitesh Choudhary"
    )

    department : Optional[str] = "General"
    salary : float = Field(
        ...,
        ge=10000, # greater than or equal to
        #le=1000000, # less than or equal to
        #description="Employee Salary in USD",
    )

class User(BaseModel):
    email : str = Field(  
        ...,
        regex = r''
    )

    phone : str = Field(
        ...,
        regex = r''
    )
    age : int = Field(
        ...,
        ge=0,
        le=150,
        description="Age must be between 0 and 150"
    )
    discount : float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Discount percentage between 0 and 100"
    )


