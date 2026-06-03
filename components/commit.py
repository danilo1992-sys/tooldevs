import subprocess
from components.opencode import opencode


def ejecutar_comando(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout.strip()


def commit():
    # Obtener el diff de los cambios
    diff = ejecutar_comando("git diff --staged")
    if not diff:
        diff = ejecutar_comando("git diff")
    
    if not diff:
        print("No hay cambios para commitear")
        return

    # Generar mensaje de commit con IA
    prompt = f"Genera un mensaje de commit corto y descriptivo para estos cambios:\n\n{diff[:2000]}"
    mensaje_commit = opencode(prompt)
    
    # Limpiar el mensaje (quitar comillas si las tiene)
    mensaje_commit = mensaje_commit.strip().strip('"').strip("'")
    
    # Ejecutar comandos de git
    ejecutar_comando("git add .")
    resultado = ejecutar_comando(f'git commit -m "{mensaje_commit}"')
    print(f"Commit creado: {resultado}")
    
    # Hacer push
    push_resultado = ejecutar_comando("git push")
    print(f"Push completado: {push_resultado}")

