from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

cliente = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://github.com/danilo1992-sys/linkedin",
        "X-Title": "Redmee-create",
    },
)


def readme(message: str, model: str = "openai/gpt-oss-20b:free"):
    try:
        response = cliente.chat.completions.create(
            model=model, messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{e}"


def linkedin(message: str, model: str = "google/gemini-2-flash:free"):
    try:
        response = cliente.chat.completions.create(
            model=model, messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{e}"


def commits(message: str, model: str = "openai/gpt-5.4-nano:free"):
    try:
        response = cliente.chat.completions.create(
            model=model, messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{e}"
