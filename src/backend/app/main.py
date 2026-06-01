from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.init_db import create_tables
from app.api.policies import router as policies_router

app = FastAPI(
    title="Agentemotor API",
    version="1.0.0"
)

# Crear tablas al iniciar
create_tables()
# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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



