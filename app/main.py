from fastapi import FastAPI
from app.auth import auth_router
from app.routers import users, excel_upload  # Agregar el import de excel_upload
from app.database import Base, engine

# Crear las tablas en la DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas
app.include_router(auth_router.router)
app.include_router(users.router)
app.include_router(excel_upload.router, prefix="/excel", tags=["Excel"])  # Incluir el router de excel
