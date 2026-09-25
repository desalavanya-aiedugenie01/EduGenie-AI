import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured in .env")

client = genai.Client(api_key=API_KEY)


def explain_concept(concept: str) -> str:
    prompt = f"""
You are EduGenie, an AI learning assistant.

Explain the following concept in a simple and student-friendly way.

Include:
1. Simple definition
2. Key points
3. A simple example
4. Short conclusion

Concept:
{concept}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text