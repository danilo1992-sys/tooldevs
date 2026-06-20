# tooldevs

Proyecto Python CLI que automatiza tareas usando IA vía OpenRouter.

## Idioma

El proyecto está escrito en **español**. Todas las respuestas, mensajes y
código nuevo deben generarse en español.

## Estructura

```
tooldevs/
├── main.py              # Entry point CLI (menú con InquirerPy)
├── pyproject.toml        # Python 3.14+, dependencias
├── .env                  # Variables (OPENROUTER_API_KEY, etc.)
├── components/
│   ├── opencode.py       # Cliente OpenRouter, llama modelos AI
│   ├── readme.py         # Genera/actualiza README.md
│   ├── commit.py         # Commit + push a git
│   ├── linkedin.py       # Publicación en LinkedIn
│   ├── workflow.py       # Genera GitHub Actions workflows
│   ├── banner.py         # Banner de bienvenida
│   └── utils.py          # Utilidades compartidas
```

## Stack

- **Python** >= 3.14
- Dependencias: `halo`, `inquirerpy`, `openai`, `pyfiglet`, `python-dotenv`, `requests`
- **OpenRouter** como provider de modelos AI
- Los prompts se construyen con contexto del proyecto real (código fuente)

## Convenciones

- Código en español (variables, comentarios, prompts)
- Usar Halo para spinners en operaciones largas
- InquirerPy para menús interactivos
- Las funciones de componentes se importan en `main.py` y se asignan a opciones del menú
- Los secretos van en `.env` (no committear)
