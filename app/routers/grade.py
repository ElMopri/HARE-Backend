from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.grade import Grade
from app.models.student import Student
from app.models.subject import Subject
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/grades",
    tags=["Grades"],
    dependencies=[Depends(get_current_user)]
)

# Listar las notas de todos los estudiantes
@router.get("/")
def get_all_grades(db: Session = Depends(get_db)):
    grades = db.query(Grade).all()
    return grades

# Listar estudiantes de una materia específica
@router.get("/subject/{subject_id}")
def get_students_by_subject(subject_id: int, db: Session = Depends(get_db)):
    grades = db.query(Grade).filter(Grade.subject_id == subject_id).all()
    if not grades:
        raise HTTPException(status_code=404, detail="No hay estudiantes para esta materia")
    return grades

# Listar materias de un estudiante específico
@router.get("/student/{student_id}")
def get_subjects_by_student(student_id: int, db: Session = Depends(get_db)):
    grades = db.query(Grade).filter(Grade.student_id == student_id).all()
    if not grades:
        raise HTTPException(status_code=404, detail="Este estudiante no tiene materias registradas")
    return grades
