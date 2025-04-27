from app.database import engine, Base
from app.models.student import Student
from app.models.subject import Subject
from app.models.grade import Grade

# Crear las tablas en la base de datos
def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas correctamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

if __name__ == "__main__":
    create_tables()
