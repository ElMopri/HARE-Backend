from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# URL de conexión
DATABASE_URL = "postgresql://postgres:root@localhost:5432/hare"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Función para obtener la sesión de base de datos
def get_db() -> Session:
    db = SessionLocal()  # Crea una nueva sesión
    try:
        yield db  # Permite usarla como un generador
    finally:
        db.close()  # Cierra la sesión después de usarla
