import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured in .env")

client = genai.Client(api_key=API_KEY)


def answer_question(question: str) -> str:

    prompt = f"""
You are EduGenie, a helpful AI learning assistant.

Answer the student's question clearly and accurately.
Use simple language suitable for a college student.

Question:
{question}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text