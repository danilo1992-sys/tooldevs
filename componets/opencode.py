from opencode_ai import Opencode
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

cliente = Opencode(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://github.com/danilo1992-sys/linkedin",
        "X-Title": "Redmee-create",
    },
)


def opencode(message: str, model: str = "x-ia/mimo-v2.5"):
    try:
        response = cliente.chat.completions.create(
            model=model, messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{e}"
