from pydantic import BaseModel

class Product(BaseModel):
    id: int 
    name: str
    price: float
    in_stock: bool = True

# Always use type annotations
# int , float , str , bool etc ...
# set sensible default 
# "123" -> 123
# "true" -> True
# 123 => 123.0

product_one = Product(id=1, name="Green Tea", price=999.99,in_stock=True)
product_two = Product(id=2, name="Mouse", price=24.33)
# product_three = Product(name="Keyboard")
