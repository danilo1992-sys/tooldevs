# LinkedIn CLI Toolkit  

**Version:** ![Version](https://img.shields.io/badge/version-0.1.0-blue)  
**Python:** ![Python](https://img.shields.io/badge/python-%3E%3D3.14-red)  
**License:** MIT  

---  

## 📖 Descripción  

`linkedin` es una herramienta de línea de comandos escrita en Python que automatiza tres tareas frecuentes de los desarrolladores que mantienen proyectos en GitHub y se divierten compartiendo sus logros en LinkedIn:

1. **Commit inteligente** – Analiza el diff de tu repositorio, genera un mensaje de commit siguiendo la convención *Conventional Commits* mediante IA y realiza el `push` a la rama principal.  
2. **README.md automático** – Genera o actualiza un archivo `README.md` profesional y adaptado al contexto de tu proyecto usando IA.  
3. **Publicación en LinkedIn** – Crea una publicación de impacto para la sección *Experiencia* de Linkeden a partir de la URL del repositorio y de la descripción generada por IA.

Todo el proceso se basa en llamadas a modelos de lenguaje a través de **OpenRouter**, lo que permite que el sistema sea completamente **IA‑driven** y **reutilizable** en cualquier proyecto Python que utilice `halo`, `inquirerpy`, `requests` y `python-dotenv`.

---  

## 🚀 Características  

| ✅ | Característica |
|---|----------------|
| **Commit AI‑driven** | Mensajes de commit generados automáticamente con formato **Conventional Commits** y push automático. |
| **README.md dinámico** | Creación o actualización de `README.md` con descripción, tabla de características, pasos de instalación y guía de contribución. |
| **Publicación en LinkedIn** | Publica en tu perfil una descripción profesional basada en el proyecto y la URL del repositorio. |
| **CLI interactiva** | Menú sencillo con `InquirerPy` que guía al usuario paso a paso. |
| **Modular** | Cada funcionalidad está aislada en módulos (`commit.py`, `readme.py`, `linkedin.py`) y reutilizable. |
| **Sin dependencias pesadas** | Sólo 5 paquetes esenciales (`halo`, `inquirerpy`, `openai`, `python-dotenv`, `requests`). |

---  

## 🛠️ Requisitos  | Requisito | Detalle |
|-----------|----------|
| **Python** | >= **3.14** (recomendado usar un entorno virtual). |
| **Git** | El proyecto asume que el repositorio ya está inicializado con `git`. |
| **Variables de entorno** | Un archivo `.env` con las siguientes claves (ver `.env.example`):  <br/>`OPENROUTER_API_KEY` <br/>`LINKEDIN_ACCESS_TOKEN` <br/>`AUTHOR_URN` |

---  

## 📦 Instalación  

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/danilo1992-sys/linkedin.git
cd linkedin

# 2️⃣ (Recomendado) Crea y activa un entorno virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3️⃣ Instala las dependencias
pip install -r requirements.txt   # o directamente con poetry si lo prefieres
```

> **Nota:** Si tu proyecto utiliza `pyproject.toml` y `poetry`/`pip-tools`, puedes instalar con:  
> ```bash
> poetry install
> ```

---  ## ⚙️ Configuración  

1. **Crea un archivo `.env` a partir del ejemplo**  

   ```bash
   cp .env.example .env   ```

2. **Rellena las variables**  

   ```dotenv
   OPENROUTER_API_KEY="sk-or-v1-tu-api-key-aqui"
   LINKEDIN_ACCESS_TOKEN="tu-linkedin-access-token"
   AUTHOR_URN="urn:li:person:tu-person-id"
   ```

   > **⚠️ Seguridad:** Nunca compartas tu `.env` con información sensible. Añádelo a tu `.gitignore`.

---  

## 🔧 Uso rápido  

Ejecutar el script principal lanza el menú interactivo:

```bash
python main.py
```

### Flujo típico  

1. **Selecciona una opción** en el menú:  

   - `1️⃣ Generar un commit y hacer push` → Analiza tu diff, genera un mensaje de commit y lo envía a la rama remota.  
   - `2️⃣ Generar un archivo README.md y subirlo a GitHub` → Crea o actualiza `README.md` y, opcionalmente, lo añade al stage para un próximo commit.  
   - `3️⃣ Generar una publicación en LinkedIn` → Introduce la URL del repositorio y publica una descripción profesional en tu perfil.  

2. **Confirma la acción** cuando se solicite (ejemplo: ¿Agregar el README a Git?).  3. **Revisa la salida** de cada paso; todos los procesos usan animaciones de `halo` para una mejor UX.  

---  

## 📂 Estructura del proyecto  

```
linkedin/
├── .env.example                 # Plantilla de variables de entorno
├── .gitignore
├── main.py                      # Punto de entrada CLI
├── pyproject.toml               # Metadatos y dependencias
├── README.md                    # (Este archivo)
├── requirements.txt             # Lista de paquetes (si no usas poetry)
│
├── components/                  # Código modular
│   ├── commit/                  # Lógica de commit automático
│   │   └── commit.py
│   ├── readme/                  # Generación/actualización del README
│   │   └── readme.py
│   └── linkedin/                # Publicación en LinkedIn
│       └── linkedin.py
│
└── opencode.py                  # Wrapper de llamadas a OpenRouter
```

---  

## 📜 Ejemplo de `README.md` generado  

> **⚠️ Los bloques a continuación son ilustrativos; el proceso real producirá un documento adaptado a tu proyecto real.**  

```markdown
# Linked Business Network  

![Version](https://img.shields.io/badge/version-0.1.0-blue)

![Python](https://img.shields.io/badge/python-%3E%3D3.14-red)

![License](https://img.shields.io/badge/license-MIT-green)

Una herramienta CLI que automatiza commits inteligentes, genera README profesionales y publica en LinkedIn.

---  

## 🚀 Características  

- **Commit AI‑driven**: mensajes de commit generados automáticamente siguiendo *Conventional Commits*.  
- **README.md dinámico**: descripción, tabla de características, pasos de instalación y guía de contribución, todo en Markdown limpio.  
- **Publicación en LinkedIn**: crea una publicación de impacto profesional basada en tu repositorio.  ---  

## 📦 Instalación  

```bash
git clone https://github.com/danilo1992-sys/linkedin.git
cd linkedin
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## ⚙️ Configuración  

1. Copia `.env.example` a `.env` y completa las variables.  
2. Asegura que tu repositorio git esté inicializado y con seguimiento remoto.  

## 🛠️ Uso  

```bash
python main.py
```

Selecciona la opción deseada del menú interactivo.  

---  

## 🤝 Contribuir  

1. Fork el repositorio.  
2. Crea una rama descriptiva (`git checkout -b feat/feature-name`).  
3. Haz commit siguiendo la convención *Conventional Commits*.  
4. Abre un Pull Request.  

---  

## 📜 Licencia  

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---  ## 📞 Contacto  

- **Autor:** Danilo [GitHub](https://github.com/danilo1992-sys)  
- **LinkedIn:** [LinkedIn Profile](https://linkedin.com/in/danilo1992)  ---  

```

---  

## 📚 Ejemplos de comandos de uso  

```bash
# 1️⃣ Generar commit automático
python main.py               # → selecciona la opción correspondiente

# 2️⃣ Actualizar README.md (selecciona "Actualizar archivo README.md")
python main.py               # → elige la opción de README → se crea/actualiza

# 3️⃣ Publicar en LinkedInpython main.py               # → elige “Generar una publicacion en linkedin”
```

---  

## 🧪 Testing (opcional)  

En la carpeta `tests/` podrías añadir pruebas unitarias para cada módulo usando `pytest`.  
Ejemplo rápido:

```bash
pip install pytestpytest discover
```

---  

## 📦 Scripts de ayuda (opcional)  

Puedes añadir comandos a tu `pyproject.toml` para facilitar el despliegue:

```toml
[project.scripts]
linkedin = "main:main"
```

Con esto basta con ejecutar `linkedin` desde cualquier terminal dentro del proyecto.  

---  

## 🙏 Agradecimientos  

- **OpenRouter** – API unificada para múltiples modelos LLM.  - **halo**, **inquirerpy**, **requests**, **python-dotenv** – Dependencias que hacen posible una CLI agradable.  
- La comunidad de desarrolladores que creen contenido de calidad en LinkedIn.  

---  

## 📜 Historial de versiones  

| Versión | Cambios |
|---------|----------|
| 0.1.0   | Lanzamiento inicial con funcionalidad completa de commits, README y LinkedIn. |

---  

## 📄 Licencia  

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.  

---  > **¡Gracias por usar LinkedIn CLI Toolkit!**  
> Si tienes alguna sugerencia de mejora, abre un *issue* o un *pull request*. 🎉