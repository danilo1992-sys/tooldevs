from openai import OpenAI
from dotenv import load_dotenv
import os
import time

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


def _call_with_retry(model: str, message: str, max_retries: int = 3) -> str:
    for attempt in range(max_retries):
        try:
            response = cliente.chat.completions.create(
                model=model, messages=[{"role": "user", "content": message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "rate limit" in error_str.lower():
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 10
                    time.sleep(wait_time)
                    continue
            return f"Error:{e}"
    return "Error: Max retries exceeded"


def opencode(message: str, model: str = "openai/gpt-oss-20b:free"):
    return _call_with_retry(model, message)


def linkedin(message: str, model: str = "nvidia/nemotron-3-ultra-550b-a55b:free"):
    return _call_with_retry(model, message)


def commits(message: str, model: str = "openai/gpt-oss-20b:free"):
    return _call_with_retry(model, message)
