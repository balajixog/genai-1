# Pydantic is a popular Python library used for data validation, parsing, and serialization using Python type hints. 
# It helps developers ensure that incoming data matches the expected format automatically.
from pydantic import BaseModel , Field
from enum import Enum 
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
    "username": "Arun",
    "age": "22"
}

#   ** takes all key-value pairs from a dictionary and passes them as keyword arguments.

#    *  -->  unpack lists/tuples
#    ** -->  unpack dictionaries
user = User(**data)

print(user)

#Enum is used when a variable should have only a fixed set of predefined values.
# Use Enum when values are:
#     fixed
#     limited
#     predefined
#     repeated often



# ADMIN → Enum member name (usually uppercase by convention)
# "admin" → actual value stored/sent
class Role(Enum):
    ADMIN = "admin"
    USER = "user"

class Account(BaseModel):
    username: str
    role: Role

a = Account(username="Arun", role="admin")
print(Role.ADMIN.value)
print(a)