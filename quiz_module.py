import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured in .env")

client = genai.Client(api_key=API_KEY)


def generate_quiz(topic: str) -> str:
    prompt = f"""
You are EduGenie, an AI learning assistant.

Create a short quiz about the following topic.

Topic:
{topic}

Create 5 multiple-choice questions.

For each question provide:
- Question
- 4 options (A, B, C, D)
- Correct answer
- Short explanation

Keep the questions suitable for a college student.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text