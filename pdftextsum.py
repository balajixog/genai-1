from google import genai
import httpx , os 
from google.genai import types

#by use url to summarize the pdf
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
 
prompt="summarize the pdf "

doc_url=httpx.get("https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/a11final-fltpln.pdf").content
pdf_url_data= types.Part.from_bytes(
    data=doc_url,
    mime_type="application/pdf"    
    )

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[pdf_url_data,prompt],
    config=types.GenerateContentConfig(
        system_instruction="the response should be atmost of 300 words",
        temperature=0.5
    )
)

print(response.text)