from InquirerPy import prompt
from components.commit import commit


def main():
    opciones = {
        "Generar un commit y hacer push": commit,
    }

    while True:
        menu = [
            {
                "type": "list",
                "message": "Selecione una opcion",
                "choices": [
                    "Generar un commit y hacer push",
                    "Publicar repositorio en Linkedin",
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
