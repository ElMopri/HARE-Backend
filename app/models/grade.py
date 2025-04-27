from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base

# Modelo de Calificaciones
class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.codigo"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    primera_nota = Column(Float)
    segunda_nota = Column(Float)
    tercera_nota = Column(Float)
    examen_final = Column(Float)
    nota_definitiva = Column(Float)
    porcentaje_asistencia = Column(Float)

    def __repr__(self):
        return f"<Grade(student_id={self.student_id}, subject_id={self.subject_id})>"
