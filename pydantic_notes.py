# Pydantic is a popular Python library used for data validation, parsing, and serialization using Python type hints. 
# It helps developers ensure that incoming data matches the expected format automatically.
from pydantic import BaseModel , Field
# Pydantic models are created by inheriting from BaseModel
# BaseModel is a parent class that gives your class Pydantic features.
    #validation
    # type checking
    # automatic conversion
    # serialization
class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)  # use field to define constraints.
    age: int = Field(gt=18)

# Here age is str we assign but it Automatic conversion happens to int 
data = {
    "name": "Arun",
    "age": "22"
}

#   ** takes all key-value pairs from a dictionary and passes them as keyword arguments.

#    *  -->  unpack lists/tuples
#    ** -->  unpack dictionaries
user = User(**data)

print(user)