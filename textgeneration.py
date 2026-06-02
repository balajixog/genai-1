from google import genai
from google.genai import types
from PIL import Image
import os

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Load image
img = Image.open("image/ghost.png")

# Multimodal prompt (image + text)
prompt = [
    img,
    "Identify the game shown in this image."
]

# Generate response
response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction="Respond in at most 100 words.",
        temperature=0.1
    )
)

for chunk in response:
    print(chunk.text, end="")
