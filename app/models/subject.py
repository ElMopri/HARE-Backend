from sqlalchemy import Column, Integer, String
from app.database import Base

# Modelo de Materia
class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<Subject(id={self.id}, nombre={self.nombre})>"
