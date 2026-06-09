# 📦 tooldevs

**tooldevs** es una utilidad todo‑en‑uno que automatiza tres tareas comunes en el flujo de trabajo de un desarrollador:

| 📌  | Funcionalidad |
|-----|---------------|
| 🎤 **Commit inteligente** <br> → Genera mensajes de commit siguiendo la convención Conventional Commits usando IA. |
| 📄 **README automático** <br> → Crea o actualiza el archivo `README.md` con información real del proyecto. |
| 🔗 **LinkedIn post** <br> → Publica en LinkedIn una descripción concisa y emojis con el contexto real del repositorio. |

> **⚠️ Instalación y ejecución**  
> El proyecto está pensado para ejecutarse con **Python ≥ 3.14** y requiere una cuenta de OpenRouter junto a las credenciales de LinkedIn.

---

## 🚀 Características

| ✨  | Descripción |
|-----|-------------|
| **Commit inteligente** | Detecta diffs y archivos nuevos, solicita IA que genere un mensaje de commit descriptivo (máx. 50 caracteres para el título) y realiza `git add`, `git commit` y `git push`. |
| **README automático** | Analiza `pyproject.toml`, los archivos de origen y los componentes, devuelve un README profesional y lo agrega al repo. |
| **LinkedIn post** | Obtiene el contexto real del repo de GitHub y publica una publicación con emojis, stack y enlace. |
| **CLI interactiva** | Menú basado en `InquirerPy` que permite elegir la acción deseada. |
| **IA modular** | La interacción con OpenRouter está encapsulada en una función sencilla; cambiar modelo solo requiere modificar un par de líneas. |
| **Estandarizado** | El flujo sigue la convención de Conventional Commits, lo que facilita el análisis de historial y changelog. |

---

## 🛠️ Instalación

1. **Clona el repositorio**  

   ```bash
   git clone https://github.com/tu-usuario/tooldevs.git
   cd tooldevs
   ```

2. **Crea un entorno virtual** (opcional pero recomendado)

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Instala las dependencias**  

   ```bash
   pip install -r requirements.txt
   # o directamente usando pyproject.toml (PEP 517)
   pip install .
   ```

4. **Configura las variables de entorno**  

   ```bash
   cp .env.example .env
   # Edita .env con:
   # - OPENROUTER_API_KEY   → API key de OpenRouter
   # - LINKEDIN_ACCESS_TOKEN→ Token de acceso a LinkedIn
   # - AUTHOR_URN          → URN de tu perfil LinkedIn
   ```

   > **Nota**: `github_token` no es obligatorio para la mayoría de las funciones, pero es necesario si quieres que el README recoja datos desde GitHub.

5. **(Opcional) Instala `halo`** para usar spinners.  
   Se incluye en el `pyproject.toml`, pero puedes instalarlo manualmente si deseas.

---

## 📦 Uso básico

```bash
python main.py
```

Selecciona la opción que quieras:

| Opción | Acción |
|--------|--------|
| Generar un commit y hacer push | Ejecuta `commit()` → IA genera commit, se añade al repo y se hace push a la rama principal |
| Generar un archivo readme y subirlo a github | Ejecuta `readmee()` → crea/actualiza `README.md` y le pide que lo committee |
| Generar una publicación en LinkedIn | Ejecuta `linkedin()` → pide URL del repositorio y publica en LinkedIn |

---

## 🤝 Contribuir

1. **Fork** el repositorio.
2. Crea una rama con tu feature:  

   ```bash
   git checkout -b feature/nombre-del-feature
   ```

3. Implementa tu cambio y haz commits con mensajes claros siguiendo *Conventional Commits*.
4. Ejecuta el script para generar los archivos automáticos, asegúrate de que todo funcione.  
   ```bash
   python main.py
   ```

5. **Envía un Pull Request** con una descripción detallada de lo que cambiaste y los motivos.

> Tip: Si tu cambio afecta a la lógica de IA, actualiza los modelos en `components/opencode.py` y verifica que los prompts se ajusten.

---

## 📜 Licencia

MIT © 2026.  
Consulta el archivo `LICENSE` para más detalles.  

---

### 📞 Contacto

Si tienes preguntas o sugerencias, abre una issue o escríbeme directamente a `tu-email@example.com`.

¡Gracias por usar **tooldevs**! 🚀