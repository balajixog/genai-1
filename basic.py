from google import genai

client = genai.Client()   # use .env or system env orElse you can use genai.Client(api_key="")

prompt=input("Enter your prompt : ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents= prompt
)

print("The response is")
print("-" * 50)
print(response.text)
print("-" * 50)
