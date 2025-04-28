from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.student import Student
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/students",
    tags=["Students"],
    dependencies=[Depends(get_current_user)]
)

# Listar todos los estudiantes
@router.get("/")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

# Obtener un estudiante por código
@router.get("/{student_code}")
def get_student_by_code(student_code: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.codigo == student_code).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return student
