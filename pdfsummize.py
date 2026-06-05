from google import genai
import os ,pathlib ,io
from google.genai import types

#by use path  to summarize the pdf 
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
 
prompt="summarize the pdf "

doc= pathlib.Path("./balaji31.pdf").read_bytes()
pdf = types.Part.from_bytes(
    data= doc,
    mime_type="application/pdf"
)



response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[pdf,prompt],
    config=types.GenerateContentConfig(
        system_instruction="the response should be atmost of 300 words",
        temperature=0.5
    )
)

print(response.text)