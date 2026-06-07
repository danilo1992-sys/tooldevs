import requests
from dotenv import load_dotenv
import os

load_dotenv()
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    print("Error: LINKEDIN_ACCESS_TOKEN no encontrado en .env")
    exit(1)

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "LinkedIn-Version": "202506",
}

# Intenta /rest/me, si falla usa /v2/userinfo (OpenID Connect)
url = "https://api.linkedin.com/rest/me"
response = requests.get(url, headers=headers)

if response.status_code != 200:
    url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    person_id = data.get("sub") or data.get("id")
    urn = f"urn:li:person:{person_id}"
    print(f"URN: {urn}")
    print(f"Datos: {data}")
else:
    print(f"Error {response.status_code}: {response.json()}")

