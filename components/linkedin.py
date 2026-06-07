import requests
from components.opencode import opencode
import os
from dotenv import load_dotenv
from InquirerPy import prompt

load_dotenv()

ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
URN = os.getenv("AUTHOR_URN")


def linkedin():
    if not ACCESS_TOKEN or not URN:
        print("Ingrese el ACCESS_TOKEN y el URN en el archivo .dotenv")
        return

    url = "https://api.linkedin.com/rest/posts"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202606",
    }

    opciotion = [
        {"type": "input", "message": "Ingrese la url del repositorio", "name": "git"}
    ]
    result = prompt(opciotion)

    prompts = f"genera una descripcion con iconoes y hashtags para linkedin para este projecto {result}"
    msg = opencode(prompts)

    payload = {
        "author": URN,
        "commentary": msg,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
        },
        "lifecycleState": "PUBLISHED",
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 201:
            print("Publicacion realizada con exito")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de red: {e}")
