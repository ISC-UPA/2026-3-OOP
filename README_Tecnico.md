# README Técnico: Arranque de un proyecto Python limpio

Este documento explica una forma profesional y reutilizable para crear un proyecto Python con:

- estructura de carpetas clara
- imports de librerías propias sin hacks
- manejo de dependencias
- entorno virtual
- variables de entorno
- ejecución correcta desde la raíz del proyecto

---

## 1. Objetivo

La meta es mantener un proyecto ordenado, fácil de mantener y sin errores de importación por rutas relativas o `sys.path` manuales.

La regla principal es:

- todo se ejecuta desde la raíz del proyecto
- los módulos propios se importan como paquetes
- el proyecto se instala en modo editable cuando sea necesario

---

## 2. Estructura recomendada del proyecto

Una estructura típica y limpia es esta:

```text
mi_proyecto/
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
├── requirements.txt      # opcional
├── src/
│   ├── __init__.py
│   ├── mi_paquete/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── utils.py
│   │   └── main.py
│   └── otra_carpeta/
│       ├── __init__.py
│       └── modulo.py
├── tests/
│   └── test_example.py
└── data/
    └── ejemplo.csv
```

### ¿Por qué usar `src/`?

Porque ayuda a separar el código fuente del proyecto del entorno de ejecución. Esto evita confusiones al importar paquetes y facilita el mantenimiento.

---

## 3. Entorno virtual

Siempre crea un entorno virtual para cada proyecto.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Verifica la versión:

```bash
python --version
```

---

## 4. Instalar dependencias

### Opción 1: desde requirements.txt

Cuando ya tienes un proyecto con dependencias definidas, lo más simple es:

```bash
pip install -r requirements.txt
```

Ejemplo de `requirements.txt`:

```txt
pandas
numpy
python-dotenv
```

### Opción 2: instalar librerías específicas

```bash
pip install pandas numpy python-dotenv
```

### Opción 3: instalar el proyecto en modo editable

Para que Python reconozca los paquetes locales del proyecto:

```bash
python -m pip install -e .
```

Esto es lo recomendable cuando trabajas con paquetes dentro de `src/`.

---

## 4.1. Flujo recomendado para un proyecto nuevo

```bash
# 1) crear entorno virtual
python -m venv .venv

# 2) activar entorno
.venv\Scripts\Activate.ps1

# 3) instalar dependencias del proyecto
pip install -r requirements.txt

# 4) instalar el proyecto local en modo editable
python -m pip install -e .

# 5) ejecutar el módulo principal
python -m mi_paquete.main
```

Esto deja el proyecto listo para desarrollar y mantenerlo sin conflictos de importación.

---

## 5. Archivo pyproject.toml

Este archivo es la base moderna para configurar un proyecto Python.

Ejemplo limpio:

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "mi-proyecto"
version = "0.1.0"
description = "Proyecto Python profesional"
requires-python = ">=3.10"

[tool.setuptools.packages.find]
where = ["."]
include = ["src*"]
```

### ¿Qué hace esto?

- define cómo se construye el proyecto
- permite instalarlo con `pip install -e .`
- hace que Python encuentre los paquetes dentro de `src/`
- evita tener que manipular `sys.path` manualmente

---

## 6. Cómo importar librerías propias

La forma correcta es importar como paquete, no con rutas relativas ni con `sys.path`.

### Ejemplo

Supongamos esta estructura:

```text
src/
├── __init__.py
├── mi_paquete/
│   ├── __init__.py
│   ├── config.py
│   └── utils.py
└── app/
    ├── __init__.py
    └── main.py
```

### En `config.py`

```python
DATABASE_NAME = "mi_bd"
```

### En `utils.py`

```python
from mi_paquete.config import DATABASE_NAME


def saludo():
    return f"Conectando a {DATABASE_NAME}"
```

### En `main.py`

```python
from mi_paquete.utils import saludo


if __name__ == "__main__":
    print(saludo())
```

### Ejecutar correcto

Desde la raíz del proyecto:

```bash
python -m app.main
```

o, si el paquete principal está en `src/mi_paquete/main.py`:

```bash
python -m mi_paquete.main
```

> Importante: no se recomienda ejecutar directamente un archivo dentro de `src` con `python src/mi_paquete/main.py` si se quiere usar importación limpia.

---

## 7. Cómo ejecutar el proyecto

La forma profesional es siempre desde la raíz del proyecto:

```bash
python -m mi_paquete.main
```

o

```bash
python -m app.main
```

Esto asegura que Python tenga el proyecto en el `sys.path` correcto.

---

## 8. Manejo de variables de entorno

Para secretos o datos sensibles, usa `.env` y `python-dotenv`.

### 1) Instalar

```bash
pip install python-dotenv
```

### 2) Crear `.env`

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=secret
```

### 3) Cargarlo en Python

```python
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
```

### 4) Ignorar el archivo en Git

En `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## 9. .gitignore recomendado

```gitignore
# entornos virtuales
.venv/
venv/

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd

# archivos de sistema
.DS_Store
Thumbs.db

# variables de entorno
.env

# build artifacts
build/
dist/
*.egg-info/
```

---

## 10. Recomendaciones de estilo

- usa nombres descriptivos en snake_case
- usa archivos pequeños y con responsabilidad única
- evita `sys.path.append(...)`
- importa desde paquetes, no desde rutas locales arbitrarias
- usa `__init__.py` para estructurar paquetes
- usa `python -m ...` para ejecutar módulos

---

## 11. Ejemplo completo de proyecto

```text
mi_proyecto/
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── mi_paquete/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── services.py
│   │   └── main.py
│   └── tools/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   └── test_services.py
└── data/
    └── sample.csv
```

### `src/config.py`

```python
DEBUG = True
APP_NAME = "Mi Proyecto"
```

### `src/mi_paquete/database.py`

```python
class Database:
    def __init__(self, name):
        self.name = name

    def connect(self):
        return f"Conectado a {self.name}"
```

### `src/mi_paquete/main.py`

```python
from config import APP_NAME
from mi_paquete.database import Database


if __name__ == "__main__":
    db = Database("mi_bd")
    print(APP_NAME)
    print(db.connect())
```

---

## 12. Errores comunes y cómo evitarlos

### Error: `ModuleNotFoundError`

Esto suele pasar cuando:

- se ejecuta un archivo directo desde una subcarpeta
- no hay un paquete bien estructurado
- no se ha instalado el proyecto en modo editable

Solución:

```bash
python -m pip install -e .
python -m mi_paquete.main
```

### Error: importación con rutas manuales

Evita cosas como:

```python
import sys
sys.path.append("C:/ruta/incorrecta")
```

Eso complica el proyecto y rompe escalabilidad.

---

## 13. Comandos útiles rápidos

```bash
# crear entorno virtual
python -m venv .venv

# activar entorno
.venv\Scripts\Activate.ps1

# instalar dependencias
pip install -r requirements.txt

# instalar proyecto editable
python -m pip install -e .

# ejecutar paquete
python -m mi_paquete.main

# ejecutar tests
pytest
```

---

## 14. Regla final

Para cualquier proyecto serio:

- usa entorno virtual
- usa `pyproject.toml`
- organiza código en `src/`
- usa imports de paquetes
- ejecuta con `python -m ...`
- usa `.env` para secretos
- no uses rutas manuales ni `sys.path`

Con esto tendrás un proyecto mucho más ordenado, reutilizable y profesional.
