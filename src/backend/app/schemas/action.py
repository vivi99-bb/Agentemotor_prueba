from pydantic import BaseModel

class ActionRequest(BaseModel):
    notes: str