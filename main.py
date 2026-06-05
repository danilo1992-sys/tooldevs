from InquirerPy import prompt
from components.commit import commit
from components.readme import readmee


def main():
    opciones = {
        "Generar un commit y hacer push": commit,
        "Generar un archivo readme y subirlo a github": readmee,
    }

    while True:
        menu = [
            {
                "type": "list",
                "message": "Selecione una opcion",
                "choices": [
                    "Generar un commit y hacer push",
                    "Generar un archivo readme y subirlo a github"
                    "Generar una publicacion en linkedin",
                    "Salir",
                ],
                "name": "opcion",
            }
        ]
        result = prompt(menu)
        opcion = result["opcion"]

        if opcion == "Salir":
            break

        if opcion in opciones:
            opciones[opcion]()
        else:
            print(f"[!]Opcion '{opcion}'")


if __name__ == "__main__":
    main()
