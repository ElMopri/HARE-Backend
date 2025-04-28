from fastapi import FastAPI
from app.auth import auth_router
from app.routers import users, student, subject, grade, excel_upload, report
from app.database import Base, engine

# Crear las tablas en la DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas
app.include_router(auth_router.router)
app.include_router(users.router)
app.include_router(student.router)
app.include_router(subject.router)
app.include_router(grade.router)
app.include_router(excel_upload.router)
app.include_router(report.router)
