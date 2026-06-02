from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-2.5-flash"
)

print("Chat session starts now...")
print("Type 'endchat' to close the session.\n")

userinput = input("user: ")

while userinput.lower() != "endchat":

    response = chat.send_message(userinput)

    print("bot:", response.text)

    userinput = input("user: ")

print("\n------ Chat History ------")

for message in chat.get_history():
    print(f"Role --> {message.role}")

    for part in message.parts:
        if hasattr(part, "text") and part.text:
            print(f"bot --> {part.text}")

    print("-" * 30)