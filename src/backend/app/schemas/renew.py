from datetime import date
from pydantic import BaseModel

class RenewRequest(BaseModel):
    new_expiration_date: date