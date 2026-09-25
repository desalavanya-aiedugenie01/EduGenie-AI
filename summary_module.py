import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured in .env")

client = genai.Client(api_key=API_KEY)


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an AI learning assistant.

Summarize the following text clearly for a college student.

Requirements:
- Keep the important points
- Use simple language
- Use bullet points where helpful
- Do not change the meaning
- Keep the summary concise

Text:
{text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text