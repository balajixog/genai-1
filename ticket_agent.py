from google import genai
import os, json
from pydantic import BaseModel
from google.genai import types
from typing import Optional
import time 

class Plan_steps(BaseModel):
    step_name: str
class Executetask(BaseModel):
    task_name:str
    action_performed:str
    summary:str
    simulated_data:Optional[str]=None

def execute_step(step):

    print('-' * 90)

    action_prompt = f"""
    Execute the task: {step}

    Describe:
    - what you did
    - summary
    - simulated data if needed
    """

    result = callmodel(action_prompt, Executetask)

    print("Task :", result.task_name)
    print("Action :", result.action_performed)
    print("Summary :", result.summary)

    if result.simulated_data:
        print("Data :", result.simulated_data)

    print('-' * 90)




def callmodel(prompt, schema):

    while True:

        try:
            response = chat.send_message(
                prompt,
                config=types.GenerateContentConfig(
                    response_schema=schema,
                    response_mime_type="application/json",
                    system_instruction="Answer within 50 words"
                )
            )
            time.sleep(10)
            return response.text
        
        except Exception as e:
            print("\nAPI ERROR:", e)
            print("Waiting 40 seconds before retry...\n")
            time.sleep(40)


def plan_goal():
    plan_prompt = f"Break the goal into clear numbered steps: {goal}"

    plans = callmodel(plan_prompt, list[Plan_steps])

    plans = json.loads(plans)

    steps = [
        plan['step_name'].strip()
        for plan in plans
        if plan['step_name'].strip()
    ]

    return steps


def run_agent():
    steps = plan_goal()

    for step in steps:
        execute_step(step)


if __name__ == "__main__":

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    model = "gemini-2.5-flash"

    goal = "Booking a ticket from Tamilnadu to Japan"

    chat = client.chats.create(
        model=model
    )

    print(f"Goal: {goal}")

    modified_goal = """
    You are an expert ticket booking agent.
    Going forward I will ask you to create and execute plans.
    """

    chat.send_message(modified_goal)
    time.sleep(15)
    run_agent()