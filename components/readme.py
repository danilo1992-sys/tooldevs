from components.commit import commit
from components.opencode import opencode
from InquirerPy import prompt
from halo import Halo
import os


LENGUAJES = [
    {
        "nombre": "Python",
        "configs": [
            "pyproject.toml",
            "setup.py",
            "setup.cfg",
            "Pipfile",
            "requirements.txt",
        ],
        "entry_points": ["main.py", "app.py", "__main__.py", "cli.py", "run.py"],
        "extensiones": [".py", ".pyx"],
    },
    {
        "nombre": "Node.js",
        "configs": ["package.json", "package-lock.json"],
        "entry_points": [
            "index.js",
            "index.ts",
            "app.js",
            "main.js",
            "cli.js",
            "server.js",
        ],
        "extensiones": [".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"],
    },
    {
        "nombre": "Rust",
        "configs": ["Cargo.toml"],
        "entry_points": ["src/main.rs", "src/lib.rs"],
        "extensiones": [".rs"],
    },
    {
        "nombre": "Go",
        "configs": ["go.mod", "go.sum"],
        "entry_points": ["main.go", "cmd/main.go"],
        "extensiones": [".go"],
    },
    {
        "nombre": "Java / Kotlin",
        "configs": ["pom.xml", "build.gradle", "build.gradle.kts", "settings.gradle"],
        "entry_points": [],
        "extensiones": [".java", ".kt", ".kts"],
    },
    {
        "nombre": "Ruby",
        "configs": ["Gemfile", "Gemfile.lock", "*.gemspec"],
        "entry_points": ["main.rb", "app.rb", "config.ru"],
        "extensiones": [".rb", ".erb"],
    },
    {
        "nombre": "PHP",
        "configs": ["composer.json", "composer.lock"],
        "entry_points": ["index.php", "app.php"],
        "extensiones": [".php"],
    },
    {
        "nombre": "Dart / Flutter",
        "configs": ["pubspec.yaml"],
        "entry_points": ["lib/main.dart", "bin/main.dart"],
        "extensiones": [".dart"],
    },
    {
        "nombre": "Elixir",
        "configs": ["mix.exs"],
        "entry_points": ["lib/", "mix.exs"],
        "extensiones": [".ex", ".exs"],
    },
    {
        "nombre": "C / C++",
        "configs": ["Makefile", "CMakeLists.txt", "meson.build", "configure.ac"],
        "entry_points": ["main.c", "main.cpp", "main.cxx"],
        "extensiones": [".c", ".cpp", ".cxx", ".h", ".hpp"],
    },
    {
        "nombre": "C# / .NET",
        "configs": ["*.csproj", "*.sln", "nuget.config"],
        "entry_points": ["Program.cs", "Main.cs"],
        "extensiones": [".cs", ".razor", ".blazor"],
    },
    {
        "nombre": "Swift",
        "configs": ["Package.swift"],
        "entry_points": ["main.swift", "Sources/"],
        "extensiones": [".swift"],
    },
]


def _detectar_lenguaje():
    for lang in LENGUAJES:
        for cfg in lang["configs"]:
            if cfg.startswith("*"):
                if list(Path(".").glob(cfg)):
                    return lang
            elif os.path.exists(cfg):
                return lang
    return None


def _leer_entry_points(lenguaje):
    contenido = ""
    for ep in lenguaje["entry_points"]:
        if os.path.exists(ep):
            with open(ep, "r") as f:
                contenido += f"{ep}:\n{f.read()}\n\n"
    return contenido


def _leer_archivos_fuente(lenguaje):
    contenido = ""
    max_archivos = 10
    max_total_bytes = 50000
    total = 0
    count = 0

    for root, dirs, files in os.walk("."):
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(
                (
                    ".",
                    "__",
                    "node_modules",
                    "venv",
                    ".venv",
                    "target",
                    "build",
                    "dist",
                    ".git",
                )
            )
        ]
        for file in files:
            if any(file.endswith(ext) for ext in lenguaje["extensiones"]):
                if count >= max_archivos or total >= max_total_bytes:
                    return contenido
                ruta = os.path.join(root, file)
                try:
                    with open(ruta, "r") as f:
                        texto = f.read(10000)
                    contenido += f"{ruta}:\n{texto}\n\n"
                    total += len(texto)
                    count += 1
                except Exception:
                    pass
    return contenido


def _leer_config(lenguaje):
    for cfg in lenguaje["configs"]:
        if cfg.startswith("*"):
            archivos = list(Path(".").glob(cfg))
            if archivos:
                with open(archivos[0], "r") as f:
                    return f"{archivos[0].name}:\n{f.read()}"
        elif os.path.exists(cfg):
            with open(cfg, "r") as f:
                return f"{cfg}:\n{f.read()}"
    return ""


def leer_contexto_proyecto():
    from pathlib import Path

    lenguaje = _detectar_lenguaje()
    contexto = []

    if lenguaje:
        contexto.append(f"Lenguaje detectado: {lenguaje['nombre']}")
        config = _leer_config(lenguaje)
        if config:
            contexto.append(config)
        entry = _leer_entry_points(lenguaje)
        if entry:
            contexto.append(entry)
        src = _leer_archivos_fuente(lenguaje)
        if src:
            contexto.append(src)

    if os.path.exists(".env.example"):
        with open(".env.example", "r") as f:
            contexto.append(f"Variables de entorno (.env.example):\n{f.read()}")

    return "\n".join(contexto) if contexto else "No se detectó un proyecto reconocible."


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
