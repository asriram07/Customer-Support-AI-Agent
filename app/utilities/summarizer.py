# app/utilities/summarizer.py

import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(text: str) -> str:
    """
    Generate a summary for a long text using OpenAI.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize this:\n\n{text}"}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
