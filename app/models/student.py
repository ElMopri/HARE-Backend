from sqlalchemy import Column, Integer, String
from app.database import Base

# Modelo de Estudiante
class Student(Base):
    __tablename__ = "students"

    codigo = Column(Integer, primary_key=True, index=True)
    nombres = Column(String, index=True)
    apellidos = Column(String)
    correo = Column(String, unique=True)
    tipo_documento = Column(String)
    numero_documento = Column(Integer, unique=True)
    programa_matriculado = Column(String)

    def __repr__(self):
        return f"<Student(codigo={self.codigo}, nombres={self.nombres})>"
