from components.commit import commit
from components.opencode import opencode
from InquirerPy import prompt
from halo import Halo
import os


def leer_contexto_proyecto():
    contexto = []

    if os.path.exists("pyproject.toml"):
        with open("pyproject.toml", "r") as f:
            contexto.append(f"pyproject.toml:\n{f.read()}")

    if os.path.exists("main.py"):
        with open("main.py", "r") as f:
            contexto.append(f"main.py:\n{f.read()}")

    componentes = ""
    if os.path.exists("components"):
        for archivo in os.listdir("components"):
            if archivo.endswith(".py"):
                with open(f"components/{archivo}", "r") as f:
                    componentes += f"{archivo}:\n{f.read()}\n\n"
        if componentes:
            contexto.append(f"Componentes:\n{componentes}")

    if os.path.exists(".env.example"):
        with open(".env.example", "r") as f:
            contexto.append(f"Variables de entorno (.env.example):\n{f.read()}")

    return "\n".join(contexto)


def crear():
    with Halo(text="Analizando el proyecto", spinner="dots"):
        contexto = leer_contexto_proyecto()

    with Halo(text="Generando archivo README.md", spinner="dots"):
        mensaje = f"""Actúa como un desarrollador senior. Genera un README.md profesional para este proyecto. Incluye: una descripción clara, una tabla de 'Características', una sección de 'Instalación' paso a paso, y una breve sección de 'Cómo contribuir'. Usa formato Markdown limpio y emojis sutiles donde sea necesario para mejorar la legibilidad.

CONTEXTO DEL PROYECTO:
{contexto}

INSTRUCCIONES ADICIONALES:
- Lee el contexto del proyecto arriba para entender que hace
- NO uses placeholders entre corchetes como [Nombre del Proyecto]
- Escribe el nombre real del proyecto basado en pyproject.toml
- Describe las funcionalidades reales basandote en el codigo fuente
- Lista las dependencias reales del pyproject.toml
- Explica como instalar y usar el proyecto
- Usa el idioma del codigo (si el codigo esta en espanol, escribe en espanol)
- Incluye badges de version si aplica
- Escribe un README util y real, no una plantilla generica"""
        contenido = opencode(mensaje)

    with open("README.md", "w") as f:
        f.write(contenido)
    print("README.md creado")


def update():
    with Halo(text="Analizando el proyecto", spinner="dots"):
        contexto = leer_contexto_proyecto()

    with Halo(text="Actualizando archivo README.md", spinner="dots"):
        mensaje = f"""Actúa como un desarrollador senior. Actualiza el archivo README.md profesional para este proyecto. Incluye: una descripción clara, una tabla de 'Características', una sección de 'Instalación' paso a paso, y una breve sección de 'Cómo contribuir'. Usa formato Markdown limpio y emojis sutiles donde sea necesario para mejorar la legibilidad.

CONTEXTO DEL PROYECTO:
{contexto}

INSTRUCCIONES ADICIONALES:
- Mantene la estructura existente si es buena
- Actualiza la informacion basada en el codigo fuente actual
- NO uses placeholders entre corchetes
- Asegurate de que las dependencias coincidan con pyproject.toml
- Verifica que los comandos de uso sean correctos
- Si hay nuevas funcionalidades, agregalas"""
        contenido = opencode(mensaje)

    with open("README.md", "w") as f:
        f.write(contenido)
    print("README.md actualizado")


def readmee():
    opciones = {
        "Crear archivo README.md": crear,
        "Actualizar archivo README.md": update,
    }
    while True:
        select = [
            {
                "type": "list",
                "message": "selecione una opcion",
                "name": "opcion",
                "choices": [
                    "Crear archivo README.md",
                    "Actualizar archivo README.md",
                    "Salir",
                ],
            }
        ]
        result = prompt(select)
        name = result["opcion"]

        if name == "Salir":
            break

        if name in opciones:
            opciones[name]()
        else:
            print(f"[!] Opcion no encontrada")

        confirm = [
            {
                "type": "confirm",
                "message": "Desea agregar el archivo README.md a git",
                "name": "git",
                "default": True,
            }
        ]
        result = prompt(confirm)

        if result["git"]:
            commit()
        else:
            break
