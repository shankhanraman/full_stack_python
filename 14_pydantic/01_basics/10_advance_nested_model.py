from pydantic import BaseModel
from typing import List, Optional ,Union

# Optional : field can be None or missing
# Nested Model : model within a model
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] =None

# Mixed data types
class Employee(BaseModel):
    name: str
    company: Company
    previous_companies: Optional[List[Company]] = None

class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent,ImageContent]]

class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    head_quarters: Address
    branches: Optional[List[Address]] = None

# Best Practices 
# Model Organization 
# 1. Define Leaf Models first- Models with no dependencies 
# 2. Build upward - Gradually  compose more complex models
# 3. User clear naming - Make relationships obvious
# 4. Group related models - Keep models in logical modules 


# Performance Considerations 
# 1. Deep nesting inmpacts perfromance - Keep resonable depth 
# 2. Large list of nested models - Consider pagination
# 3, Circular refernces - Use carefully , can casue major memory issues
# 4. Lazy loading  - Consider for expensive nested computations

# # Data Modeling Tips
# 1. Model real-world relationships - Mirror your domain structure 
# 2. Use optional appropriately - Not all relationships are required
# 3. Consider Union types - For polymorphic relatiosnhips
# 4. Validate buisness rules - Use model validaotrs fro cross-model logic
