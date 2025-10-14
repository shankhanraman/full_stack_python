from pydantic import BaseModel, field_validator,model_validator

class User(BaseModel):
    username: str
    password: str

    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")
        return value

class SingnUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueError("Passwords do not match")
        return values