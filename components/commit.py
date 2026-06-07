import subprocess
from components.opencode import opencode
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
        prompt = f"Genera un mensaje de commit corto y descriptivo para estos cambios:\n\n{info_cambios[:2000]}"
        mensaje_commit = opencode(prompt)

    mensaje_commit = mensaje_commit.strip().strip('"').strip("'")

    with Halo(text="Agregando archivos", spinner="dots"):
        ejecutar_comando("git add .")

    resultado = ejecutar_comando(f'git commit -m "{mensaje_commit}"')
    print(f"Commit creado: {resultado}")

    with Halo(text="Haciendo push a la rama principal", spinner="dots"):
        push_resultado = ejecutar_comando("git push")
    print(f"Push completado: {push_resultado}")
