# LinkedInCLI

![Python Version](https://img.shields.io/badge/Python-3.14%2B-blue)  
![License: MIT](https://img.shields.io/badge/License-MIT-green)  
![Version 0.1.0](https://img.shields.io/badge/version-0.1.0-blue)

## Descripción

`linkedin` es una herramienta de línea de comandos (CLI) en Python que combina la gestión de un repositorio GitHub con la generación automática de contenido para redes sociales.  

Utiliza la API de **OpenRouter** (compatible con varios modelos de lenguaje) para:

* Analizar el contexto del proyecto ( `pyproject.toml`, código fuente, componentes).  
* Generar un **README.md** profesional y actualizado.  
* Crear mensajes de *commit* claros y descriptivos mediante IA.  * Publicar en **LinkedIn** una publicación estructurada con emojis, títulos en negrita y hashtags.

---

## Características

| Funcionalidad | Qué hace | Cómo se ejecuta |
|---------------|----------|-----------------|
| **Commit inteligente** | Analiza los cambios de Git y genera un mensaje de commit corto y descriptivo mediante IA. | Selección “Generar un commit y hacer push” en el menú. |
| **README Generator** | Crea o actualiza el archivo `README.md` con la información más reciente del proyecto. | Selección “Generar un archivo readme y subirlo a github”. |
| **LinkedIn Publisher** | Construye una publicación lista para LinkedIn (formato con emojis, negritas y hashtags) y la envía usando la API de LinkedIn. | Selección “Generar una publicacion en linkedin”. |

---

## Instalación

```bash
# Clona el repositorio
git clone https://github.com/danilo1992-sys/linkedin.git
cd linkedin

# Entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt   # o pip install halo inquirerpy openai python-dotenv requests
```

> **Requisitos mínimos:** Python **≥ 3.14**.

---

## Uso

Ejecuta el programa:

```bashpython main.py
```

### Menú interactivo

```
Selecione una opcion
[0] Generar un commit y hacer push[1] Generar un archivo readme y subirlo a github
[2] Generar una publicacion en linkedin
[3] Salir
> 
```

#### 1️⃣ Generar un commit y hacer push
* Analiza los cambios (`git diff`), crea un mensaje de commit mediante IA y ejecuta el *push* a la rama actual.

#### 2️⃣ Generar un archivo README.md y subirlo a GitHub
* Analiza el proyecto, escribe un `README.md` profesional y lo guarda en el directorio raíz.  
* Después se puede añadir el archivo al stage y hacer commit automáticamente.

#### 3️⃣ Generar una publicación en LinkedIn
* Pide la URL del repositorio y genera una publicación con el siguiente formato:

```
🚀 **Nombre del Proyecto** - Breve descripcion del proyecto

Primera linea explicando que es la herramienta y que hace.

⚡ **Sección principal:**
- 🚀 **Commit inteligente** - Genera mensajes de commit automáticos.
- 📄 **README Generator** - Crea/actualiza el README.md.
- 🔗 **LinkedIn Publisher** - Publica en LinkedIn con formato estructurado.

🛠 **Tecnologias:**
- halo
- inquirerpy
- openai (OpenRouter)
- python-dotenv
- requests

💡 **Cierre:** Herramienta ideal para equipos que buscan automatizar documentación y difusión en redes.

#LinkedIn #DevOps #Python #AI #OpenSource
```

* Luego, mediante la API de LinkedIn, se publica el contenido.

---

## Configuración

1. **Variables de entorno**  
   Copia `.env.example` a `.env` y completa los campos:

   ```dotenv
   OPENROUTER_API_KEY="sk-..."          # clave para la API de OpenRouter
   LINKEDIN_ACCESS_TOKEN="your-token"    # token de acceso a LinkedIn
   AUTHOR_URN="urn:li:person:your-id"    # identificador del autor en LinkedIn
   ```

2. **Credenciales de LinkedIn**  
   Son obligatorias sólo si se usará la funcionalidad de publicación en LinkedIn.

3. **Estructura de directorios**  
   ```
   .
   ├── pyproject.toml
   ├── main.py
   ├── .env.example
   ├── .env               # <-- creado manualmente   ├── README.md
   └── components/
       ├── commit.py
       ├── linkedin.py
       └── ...             # otros módulos internos
   ```

---

## Dependencias| Paquete | Versión mínima | Comentario |
|---------|----------------|------------|
| `halo` | `0.0.31` | Spinners visuales en la consola. |
| `inquirerpy` | `0.3.4` | Menús interactivos en la terminal. |
| `openai` | `1.0.0` | Cliente para comunicarse con OpenRouter. |
| `python-dotenv` | `1.2.2` | Carga automática de variables `.env`. |
| `requests` | `2.34.2` | Llamadas HTTP a la API de LinkedIn. |

Todas ellas están declaradas en `pyproject.toml`.

---

## Ejemplo completo

```bash
$ python main.py
Selecione una opcion[0] Generar un commit y hacer push
[1] Generar un archivo readme y subirlo a github
[2] Generar una publicacion en linkedin
[3] Salir
> 2
Analizando el proyecto...
Generando archivo README.md...
README.md creado
Desea agregar el archivo README.md a git?
{
  "git": true
}
Agregando archivos...
Commit creado: bf5e2c3a7c3c7b4e8f6a1b2c3d4e5f6a7b8c9d0e
Push completado: total 0
```

---

## Contribuir

1. Haz fork del proyecto.  
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`.  
3. Implementa tus cambios y asegura que el código pase los tests.  
4. Abre un Pull Request describiendo lo realizado.

---

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

## Contacto

- **Autor:** Danilo — [GitHub](https://github.com/danilo1992-sys)  
- **Issues:** https://github.com/danilo1992-sys/linkedin/issues  

---

> *¡Gracias por usar `linkedin`! Si te gusta, comparte el proyecto y ayúdanos a mejorarlo juntos.*