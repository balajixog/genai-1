from google import genai
from google.genai import types
client = genai.Client()  

# ground tool means extra information
ground_tool=types.Tool(
    google_search=types.GoogleSearch()
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="who is the greatest  actor",
    config=types.GenerateContentConfig(
        system_instruction="atmost 200 words",
        tools=[ground_tool],
        temperature=0.2
    )
)

print(response.text)
