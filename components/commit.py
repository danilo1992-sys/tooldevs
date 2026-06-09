import subprocess
from components.opencode import commits
from halo import Halo


def ejecutar_comando(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout.strip()


def commit():
    diff = ejecutar_comando("git diff --staged")
    if not diff:
        diff = ejecutar_comando("git diff")

    untracked = ejecutar_comando("git ls-files --others --exclude-standard")

    if not diff and not untracked:
        print("No hay cambios para commitear")
        return

    with Halo(text="Generando commit con IA", spinner="dots"):
        info_cambios = diff
        if untracked:
            info_cambios += f"\n\nArchivos nuevos: {untracked}"
        prompt = f"Escribe un mensaje de commit siguiendo la convención Conventional Commits. El mensaje debe ser corto (máximo 50 caracteres para el título) seguido de una breve descripción de los cambios. Analiza este diff:\n\n{info_cambios[:2000]}"
        mensaje_commit = commits(prompt)

    mensaje_commit = mensaje_commit.strip().strip('"').strip("'")

    with Halo(text="Agregando archivos", spinner="dots"):
        ejecutar_comando("git add .")

    resultado = ejecutar_comando(f'git commit -m "{mensaje_commit}"')
    print(f"Commit creado: {resultado}")

    with Halo(text="Haciendo push a la rama principal", spinner="dots"):
        push_resultado = ejecutar_comando("git push")
    print(f"Push completado: {push_resultado}")
