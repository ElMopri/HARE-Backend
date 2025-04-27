import pandas as pd
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from io import BytesIO
from app.database import get_db
from app.models.student import Student
from app.models.subject import Subject
from app.models.grade import Grade
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/upload", dependencies=[Depends(get_current_user)])
async def upload_excel(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents = await file.read()
        excel_data = BytesIO(contents)

        # Leer todo el archivo sin fijar encabezados
        df = pd.read_excel(excel_data, engine="openpyxl", header=None)

        # Obtener nombres de columnas manualmente
        columns = [
            "Codigo",
            "Nombres",
            "Apellidos",
            "Correo",
            "Tipo de documento",
            "N de documento",
            "Programa matriculado",
        ]

        # A partir de la columna 7 (índice 7 -> columna H), siguen notas de materias
        materia_start_col = 7

        # Construir lista de materias
        materias = []
        col_idx = materia_start_col
        while col_idx < df.shape[1]:
            materia_name = df.iloc[0, col_idx]  # Fila 1
            materias.append((materia_name, col_idx))
            col_idx += 6  # Porque cada materia ocupa 6 columnas

        # Filtrar solo filas de datos (desde fila 2 hacia abajo)
        data_rows = df.iloc[2:]  # fila 3 en Excel (índice 2 en pandas)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer el archivo Excel: {str(e)}")

    try:
        for idx, row in data_rows.iterrows():
            if pd.isna(row[0]):
                continue  # Saltar filas vacías

            student = db.query(Student).filter(Student.codigo == int(row[0])).first()
            if not student:
                student = Student(
                    codigo=int(row[0]),
                    nombres=row[1],
                    apellidos=row[2],
                    correo=row[3],
                    tipo_documento=row[4],
                    numero_documento=int(row[5]),
                    programa_matriculado=row[6],
                )
                db.add(student)
                db.commit()
                db.refresh(student)

            for materia_name, start_col in materias:
                if pd.isna(materia_name):
                    continue

                materia_name = str(materia_name).strip()

                subject = db.query(Subject).filter(Subject.nombre == materia_name).first()
                if not subject:
                    subject = Subject(nombre=materia_name)
                    db.add(subject)
                    db.commit()
                    db.refresh(subject)

                grade = Grade(
                    student_id=student.codigo,
                    subject_id=subject.id,
                    primera_nota=row[start_col],
                    segunda_nota=row[start_col + 1],
                    tercera_nota=row[start_col + 2],
                    examen_final=row[start_col + 3],
                    nota_definitiva=row[start_col + 4],
                    porcentaje_asistencia=row[start_col + 5]
                )
                db.add(grade)

        db.commit()
        return {"message": "Archivo procesado y datos insertados correctamente."}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")
