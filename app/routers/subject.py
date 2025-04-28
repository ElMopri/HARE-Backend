from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.subject import Subject
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"],
    dependencies=[Depends(get_current_user)]
)

# Listar todas las materias
@router.get("/")
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    return subjects

# Obtener una materia por ID
@router.get("/{subject_id}")
def get_subject_by_id(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return subject
