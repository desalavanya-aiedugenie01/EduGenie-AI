import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured in .env")

client = genai.Client(api_key=API_KEY)


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are EduGenie, an AI learning assistant.

Create a simple learning path for the following topic:

Topic:
{topic}

Include:
1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Suggested order of learning
5. Practice activities
6. Small project ideas

Make it clear and suitable for a college student.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text