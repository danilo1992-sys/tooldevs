from components.commit import commit
from components.opencode import opencode
from InquirerPy import prompt
from halo import Halo

def crear():
    with Halo(text="Generando archivo README.md", spinner="dots"):
        mensaje = "Genera un archivo README.md de este repositorio"
        contenido = opencode(mensaje)
    with open("README.md", "w") as f:
        f.write(contenido)
    print("README.md creado")


def update():
    with Halo(text="Actualizando archivo README.md", spinner="dots"):
        mensaje = "Actualiza el archivo README.md con las nuevas caracteristicas"
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
