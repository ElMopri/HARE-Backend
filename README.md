## HARE-Backend

H.A.R.E. (Herramienta de Análisis de Rendimiento Estudiantil) es un backend desarrollado en FastAPI que recopila, procesa y expone datos académicos para mejorar la toma de decisiones en instituciones educativas.

## Tecnologías utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- JWT (Json Web Tokens) para autenticación

## Requisitos previos

- Tener Python instalado.
- Tener PostgreSQL instalado y configurado.
- Tener pip para instalar dependencias.
- Crear y configurar una base de datos llamada hare.

## INSTALACIÓN

Clona el repositorio:

`git clone https://github.com/ElMopri/HARE-Backend.git`

`cd HARE-Backend`

Crea un entorno virtual e instálalo:

`python -m venv .venv`

`source .venv/bin/activate  # Linux/Mac`

`.venv\Scripts\activate     # Windows`

Instala las dependencias:

`pip install -r requirements.txt`

Configura la conexión a la base de datos en `app/database.py`:

`DATABASE_URL = "postgresql://postgres:TU_CONTRASEÑA@localhost/hare"`

## EJECUCION DEL PROYECTO

Levanta el servidor de desarrollo:

`uvicorn app.main:app --reload`

Accede a la documentación interactiva en:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

Estructura del proyecto:

```
HARE-Backend/
├── app/
│   ├── auth/           # Manejo de autenticación
│   ├── database.py     # Configuración de la base de datos
│   ├── main.py         # Punto de entrada de la aplicación
│   ├── models/         # Modelos ORM
│   ├── routers/        # Rutas y endpoints
│   ├── schemas/        # Esquemas de Pydantic
│   └── dependencies/   # Dependencias reutilizables
├── .gitignore
├── requirements.txt
└── README.md
```

## Licencia

Este proyecto es de uso académico.
Desarrollado por Andrés Felipe López Triana y Henry Alexander Blanco Rolon.