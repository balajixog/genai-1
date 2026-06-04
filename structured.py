from google import genai
import os
from enum import Enum
from pydantic import BaseModel

client= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "give a top recipe with ingredients list"

class Grade(Enum):
      A_PLUS="a+"
      A="a"
      B="b"
      C="c"
      

class Recipe(BaseModel):
      recipe_name:str
      ingredients : list[str]
      rating : Grade

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents= prompt,
    config={
          "response_mime_type":"application/json",
          "response_schema":list[Recipe]
    }
)

print(response.text)