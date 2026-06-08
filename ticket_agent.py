from google import genai
import os
import json
from pydantic import BaseModel
from google.genai import types
from typing import Optional


class Plan_steps(BaseModel):
    step_name: str


class Executetask(BaseModel):
    task_name: str
    action_performed: str
    summary: str
    simulated_data: Optional[str]


def execute_step(step):
    print("-" * 30)

    action_prompt = f"""
    Execute the task: {step}

    Describe what you did and summarize the result.
    Simulate the steps if required.
    """

    result = callmodel(action_prompt, Executetask)

    result = json.loads(result)

    print("Task :", result["task_name"])
    print("Action :", result["action_performed"])
    print("Summary :", result["summary"])

    if result["simulated_data"]:
        print("Data :", result["simulated_data"].strip())

    print("-" * 30)


def callmodel(prompt, schema):
    response = chat.send_message(
        prompt,
        config=types.GenerateContentConfig(
            response_schema=schema,
            response_mime_type="application/json",
            system_instruction="Answer within 50 words"
        )
    )

    return response.text


def plan_goal():
    plan_prompt = f"""
    Break the goal into clear numbered steps:
    {goal}
    """

    plans = callmodel(plan_prompt, list[Plan_steps])

    plans = json.loads(plans)

    steps = [
        plan["step_name"].strip()
        for plan in plans
        if plan["step_name"].strip()
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

    run_agent()