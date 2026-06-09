import requests
from components.opencode import linkedin as linkedin_ai
import os
from dotenv import load_dotenv
from InquirerPy import prompt
from halo import Halo

load_dotenv()

ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
URN = os.getenv("AUTHOR_URN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def fetch_repo_context(repo_url: str) -> str:
    if not GITHUB_TOKEN:
        return ""
    try:
        parts = repo_url.rstrip("/").split("/")
        owner, repo = parts[-2], parts[-1].replace(".git", "")
        headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
        
        readme_resp = requests.get(f"https://api.github.com/repos/{owner}/{repo}/readme", headers=headers)
        readme = ""
        if readme_resp.status_code == 200:
            import base64
            readme = base64.b64decode(readme_resp.json()["content"]).decode("utf-8")[:3000]
        
        contents_resp = requests.get(f"https://api.github.com/repos/{owner}/{repo}/contents", headers=headers)
        files = []
        if contents_resp.status_code == 200:
            files = [f["name"] for f in contents_resp.json() if f["type"] == "file"][:20]
        
        lang_resp = requests.get(f"https://api.github.com/repos/{owner}/{repo}/languages", headers=headers)
        languages = list(lang_resp.json().keys()) if lang_resp.status_code == 200 else []
        
        return f"README:\n{readme}\n\nArchivos principales: {', '.join(files)}\n\nLenguajes: {', '.join(languages)}"
    except Exception:
        return ""


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

    opcion = [
        {"type": "input", "message": "Ingrese la url del repositorio", "name": "git"}
    ]
    result = prompt(opcion)
    repo_url = result["git"]

    with Halo(text="Obteniendo contexto del repositorio...", spinner="dots"):
        repo_context = fetch_repo_context(repo_url)

    prompt_text = f"""Genera una publicación corta para LinkedIn (máx. 3500 caracteres) con emojis sobre este repositorio real.

URL: {repo_url}

Contexto real del repositorio:
{repo_context}

Escribe una publicación auténtica basada en ESTE contenido real (no plantillas genéricas). Incluye: qué hace exactamente, stack tecnológico real, y link al repo. Sé conciso y directo."""

    with Halo(text="Generando publicacion con IA", spinner="dots"):
        msg = linkedin_ai(prompt_text)

    commentary = f"{msg}\n\n{repo_url}"
    if len(commentary) > 3900:
        commentary = commentary[:3897] + "..."

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
