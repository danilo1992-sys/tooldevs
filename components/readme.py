from components.commit import commit
from components.opencode import opencode
from InquirerPy import promt

def crear():
     promt = "Genera un archivo README.md de este repositorio"
    opencode(promt)   

def update():
    promt = "Actualiza el archivo README.md con la nuevas carateristicas"
    opencode(promt)
def readmee():
    opciones = {
        "Creat archivo README.md": crear(),
        "Actualizar archivo READMEE.md": update(),
    }
    while True:
        select = [
            {
                "type": "select",
                "mensaje": "selecione una opcion",
                "name":"name", 
                "choices": [
                    "Crear archivo READMEE.md",
                    "Actualizar archivo READMEE.md",
                    "Salir", 
                ],
            }
        ]
        result = promt(select)
        name = result['name']

        if opciones == "Salir": 
             break

        if opcion in opciones:
            opciones[opcion]()
        else: 
            print(f"[!] Opcion no encontrada")

        confirm = [
            {
            "type":"confirm",
            "mensaje":"Desea agregar el archivo READMEE.md a git",
            "name":"git",
            "default":"True",
            }
        ]
        result = promt(confirm)
            
        if result["git"]:
            commit()
        else:
            break
