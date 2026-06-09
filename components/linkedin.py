import requests
from components.opencode import linkedin
import os
from dotenv import load_dotenv
from InquirerPy import prompt
from halo import Halo

load_dotenv()

ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
URN = os.getenv("AUTHOR_URN")


def linkedin():
    if not ACCESS_TOKEN or not URN:
        print("Ingrese el ACCESS_TOKEN y el URN en el archivo .env")
        return

    url = "https://api.linkedin.com/rest/posts"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202604",
    }

    opciotion = [
        {"type": "input", "message": "Ingrese la url del repositorio", "name": "git"}
    ]
    result = prompt(opciotion)
    repo_url = result["git"]

    prompt_text = f"""Actúa como un experto en Personal Branding para perfiles técnicos. Escribe una descripción de impacto para mi sección de 'Experiencia' en LinkedIn sobre este proyecto/cargo. Enfócate en resultados, tecnologías clave utilizadas y el impacto técnico. Mantén un tono profesional pero entusiasta. No uses clichés excesivos."""

    with Halo(text="Generando publicacion con IA", spinner="dots"):
        msg = opencode(prompt_text)

    commentary = f"{msg}\n\n{repo_url}"

    payload = {
        "author": URN,
        "commentary": commentary,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
        },
        "lifecycleState": "PUBLISHED",
    }

    with Halo(text="Publicando en LinkedIn", spinner="dots"):
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 201:
                print("Publicacion realizada con exito")
            else:
                print(f"Error {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error de red: {e}")
