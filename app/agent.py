import google.generativeai as genai

from app.config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


def run_agent(task: str):

    prompt = f"""
You are an intelligent AI Agent.

Solve the following task.

Task:
{task}

Provide a clear and concise answer.
"""

    response = model.generate_content(prompt)

    return response.text
