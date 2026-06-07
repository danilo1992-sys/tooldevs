import requests
from components.opencode import opencode
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

    prompt_text = f"""Genera una publicacion para LinkedIn sobre este repositorio de GitHub: {repo_url}

Sigue EXACTAMENTE este formato y estilo:

🚀 **Nombre del Proyecto** - Breve descripcion del proyecto

Primera linea explicando que es la herramienta y que hace.

⚡ **Seccion principal (ej: Features/Frameworks/Caracteristicas):**
- Emoji **Nombre** - Descripcion corta
- Emoji **Nombre** - Descripcion corta
- Emoji **Nombre** - Descripcion corta

🛠 **Tecnologias:**
- Bullet point con tecnologias usadas

💡 **Cierre:** Frase para desarrolladores o usuarios ideales

IMPORTANTE:
- Usa emojis al inicio de cada linea
- Usa negrita con **texto** para titulos de seccion
- Usa - o • para listas
- NO uses ## para titulos
- Termina con 15 hashtags separados por espacio usando el formato hashtag#Palabra
- No pongas saltos de linea dobles excesivos
- El tono debe ser profesional pero amigable
- Menciona las tecnologias principales que uses en el proyecto"""

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
