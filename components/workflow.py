from InquirerPy import prompt as inquirer_prompt
from components.opencode import workflow as generar_con_ia
from components.commit import commit
from halo import Halo


def docker():
    prompt_text = """Genera un workflow de GitHub Actions (YAML válido) para build y push de imagen Docker.
    Requisitos del workflow:
    - actions/checkout@v4, docker/setup-buildx-action@v3, docker/login-action@v3, docker/metadata-action@v5, docker/build-push-action@v6
    - Cache de capas: cache-from/cache-to con GitHub Actions cache
    - Tags: latest + SHA corto (docker/metadata-action)
    - Secrets: explica qué configurar en Settings > Secrets
    - Permisos: contents: read, packages: write (si aplica)

    Incluye explicación breve de cada step y la lista de secrets necesarios."""

    with Halo(text="Generando workflow Docker con IA", spinner="dots"):
        msg = generar_con_ia(prompt_text)

    print(msg)
    commit()
    return msg


def releases():
    prompt_text = """Genera un workflow de GitHub Actions (YAML válido) para crear GitHub Releases automáticos.
    Requisitos del workflow:
    - actions/checkout@v4
    - Disparador (on): push de tags con patrón v* (ej: v1.0.0, v0.2.3)
    - Usar softprops/action-gh-release@v2 para crear el release
    - Generar changelog automático entre tags (sugerencia: extraer de Conventional Commits con un paso previo)
    - Compilar binarios de la aplicación y subirlos como assets del release
    - Publicar en PyPI, npm, crates.io o similar (opcional pero valorado)
    - Firma de checksums (SHA256) de los artifacts

    Incluye explicación breve de cada step, lista de permisos necesarios (contents: write) y cómo funciona GITHUB_TOKEN automáticamente."""

    with Halo(text="Generando workflow Releases con IA", spinner="dots"):
        msg = generar_con_ia(prompt_text)

    print(msg)
    commit()
    return msg


def workflow():
    opciones = {
        "Generar workflow para docker": docker,
        "Generar workflow para releases": releases,
    }

    while True:
        menu = [
            {
                "type": "list",
                "name": "opcion",
                "message": "Seleccione una opcion",
                "choices": [
                    "Generar workflow para docker",
                    "Generar workflow para releases",
                    "Salir",
                ],
            }
        ]
        result = inquirer_prompt(menu)
        opcion = result["opcion"]

        if opcion == "Salir":
            break

        if opcion in opciones:
            opciones[opcion]()
        else:
            print(f"[!] Opcion '{opcion}' no valida")


if __name__ == "__main__":
    workflow()
