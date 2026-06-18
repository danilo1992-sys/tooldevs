import os
import re

from InquirerPy import prompt as inquirer_prompt
from components.opencode import workflow as generar_con_ia
from components.commit import commit
from halo import Halo

WORKFLOW_DIR  = ".github/workflows"


def _extraer_yaml(texto: str) -> str | None:
    """Extrae YAML de la respuesta de la IA, manejando codeblocks."""
    block = re.search(
        r"```(?:yaml|yml)?\s*\n?(.*?)```", texto, re.DOTALL
    ) or re.search(r"^---\n(.*?)(?:^---|\Z)", texto, re.DOTALL)
    return block.group(1).strip() if block else texto.strip()


def _nombre_workflow(yaml_content: str) -> str:
    """Extrae el nombre del workflow del YAML vía regex para usarlo como filename."""
    m = re.search(r'^name\s*:\s*(.+)$', yaml_content, re.MULTILINE)
    nombre = m.group(1).strip().strip('"').strip("'") if m else "workflow"
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", nombre).strip("-").lower()


def _escribir_workflow(yaml_content: str, nombre_base: str):
    """Escribe el YAML en .github/workflows/<nombre>.yml."""
    os.makedirs(WORKFLOW_DIR, exist_ok=True)
    ruta = os.path.join(WORKFLOW_DIR, f"{nombre_base}.yml")

    with open(ruta, "w") as f:
        f.write(yaml_content)

    print(f" Workflow guardado en {ruta}")
    return ruta


def docker():
    prompt_text = """Genera un workflow de GitHub Actions (YAML válido) para build y push de imagen Docker.
    Requisitos del workflow:
    - actions/checkout@v4, docker/setup-buildx-action@v3, docker/login-action@v3, docker/metadata-action@v5, docker/build-push-action@v6
    - Cache de capas: cache-from/cache-to con GitHub Actions cache
    - Tags: latest + SHA corto (docker/metadata-action)
    - Secrets: explica qué configurar en Settings > Secrets
    - Permisos: contents: read, packages: write (si aplica)

    Devuelve SOLO el YAML, sin explicaciones ni markdown."""

    with Halo(text="Generando workflow Docker con IA", spinner="dots"):
        respuesta = generar_con_ia(prompt_text)

    yaml_content = _extraer_yaml(respuesta)
    nombre = _nombre_workflow(yaml_content)
    _escribir_workflow(yaml_content, nombre)
    commit()


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
    - Permisos: contents: write

    Devuelve SOLO el YAML, sin explicaciones ni markdown."""

    with Halo(text="Generando workflow Releases con IA", spinner="dots"):
        respuesta = generar_con_ia(prompt_text)

    yaml_content = _extraer_yaml(respuesta)
    nombre = _nombre_workflow(yaml_content)
    _escribir_workflow(yaml_content, nombre)
    commit()


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
