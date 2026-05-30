from google import genai
import os
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))   # use .env or system env orElse you can use genai.Client(api_key="")

prompt=input("Enter your prompt : ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents= prompt,
    config= types.GenerateContentConfig(
        system_instruction="your response should be within 50 words",
        temperature= 2            #simply it about how much creativity you want. | less means low creativity fast response. | high means more creativity and slow response. 
        
    )
)

print("The respense is ")
print("-----------------------------------------------------")
print(response.text)
print("-----------------------------------------------------")
