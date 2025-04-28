from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.student import Student
from app.models.grade import Grade
from app.models.subject import Subject
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/report",
    tags=["Report"],
    dependencies=[Depends(get_current_user)]
)

# Endpoint 1: Obtener un estudiante específico con sus materias y notas
@router.get("/student/{student_codigo}")
def get_student_by_codigo(student_codigo: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.codigo == student_codigo).first()

    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado.")

    grades = db.query(Grade).filter(Grade.student_id == student_codigo).all()

    materias = []
    for grade in grades:
        subject = db.query(Subject).filter(Subject.id == grade.subject_id).first()
        if subject:
            materias.append({
                "nombre_materia": subject.nombre,
                "primera_nota": grade.primera_nota,
                "segunda_nota": grade.segunda_nota,
                "tercera_nota": grade.tercera_nota,
                "examen_final": grade.examen_final,
                "nota_definitiva": grade.nota_definitiva,
                "porcentaje_asistencia": grade.porcentaje_asistencia
            })

    return {
        "codigo": student.codigo,
        "nombres": student.nombres,
        "apellidos": student.apellidos,
        "correo": student.correo,
        "programa_matriculado": student.programa_matriculado,
        "materias": materias
    }

# Endpoint 2: Obtener estudiantes de una materia específica
@router.get("/subject/{subject_id}")
def get_students_by_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Materia no encontrada.")

    grades = db.query(Grade).filter(Grade.subject_id == subject_id).all()

    estudiantes = []
    for grade in grades:
        student = db.query(Student).filter(Student.codigo == grade.student_id).first()
        if student:
            estudiantes.append({
                "codigo": student.codigo,
                "nombres": student.nombres,
                "apellidos": student.apellidos,
                "correo": student.correo,
                "primera_nota": grade.primera_nota,
                "segunda_nota": grade.segunda_nota,
                "tercera_nota": grade.tercera_nota,
                "examen_final": grade.examen_final,
                "nota_definitiva": grade.nota_definitiva,
                "porcentaje_asistencia": grade.porcentaje_asistencia
            })

    return {
        "materia": subject.nombre,
        "estudiantes": estudiantes
    }
