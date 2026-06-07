import requests

ACCESS_TOKEN = "AQWLoBkpjlFjjwJz_BH-0yb3gFM5V5-4soseXVKZ2jtrIPBkPmRMPPdz5dek2Nc18JiclJ7MqYgjceEdk8AJp3FciFLnb0ST2UfE_AyFAgG0gyHJ3Zn8yvDY251gKcSlk9IU0p-NHjMvTm3PhCOuU2TA9P-iXdeXErWpbQaPVYpHj1lkuc8jaIERCngDWmf0u-P4lP1796UjAf1eeiN75EI8gqKCSxId4Omkb06YOcz-fNckIFptfjbqgmuFBB13VlJmiOwA9sFsl_vVWGIiOdbOYfbaIPk_5VOE5I0h6iCLa8ihsjR7yEALPE0Lb0WmiCFgfRoOoa3HjBPROPLP14xT1GxjPg"

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

