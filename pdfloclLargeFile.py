from google import genai
from google.genai import types
import pathlib
import os
import time

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

file_path = pathlib.Path("./sp-4212.pdf")

print("Uploading file...")

sample_file = client.files.upload(
    file=file_path
)

print("Uploaded:", sample_file.name)
print("State:", sample_file.state.name)

# Wait until processing finishes
while sample_file.state.name == "PROCESSING":
    print("Waiting for file processing...")
    time.sleep(5)

    sample_file = client.files.get(
        name=sample_file.name
    )

print("Final state:", sample_file.state.name)

# Important check
if sample_file.state.name != "ACTIVE":
    raise Exception(f"File failed: {sample_file.state.name}")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        sample_file,
        "Summarize this PDF in under 300 words"
    ],
    config=types.GenerateContentConfig(
        temperature=0.5,
        max_output_tokens=400
    )
)

print(response.text)