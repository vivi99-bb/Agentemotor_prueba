from fastapi import FastAPI

from app.database.init_db import create_tables

app = FastAPI()

create_tables()

@app.get("/")
def root():
    return {
        "message": "Agentemotor API"
    }