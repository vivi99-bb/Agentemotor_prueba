from fastapi import FastAPI

from app.database.init_db import create_tables
from app.api.policies import router as policies_router

app = FastAPI(
    title="Agentemotor API",
    version="1.0.0"
)

# Crear tablas al iniciar
create_tables()

# Registrar endpoints
app.include_router(
    policies_router,
    prefix="/api",
    tags=["Policies"]
)


@app.get("/")
def root():
    return {
        "message": "Agentemotor API"
    }

