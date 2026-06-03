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


def opencode(message: str, model: str = "meta-llama/llama-4-maverick:free"):
    try:
        response = cliente.chat.completions.create(
            model=model, messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{e}"
