from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.connection import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)

    client_id = Column(Integer, ForeignKey("clients.id"))

    policy_number = Column(String)
    policy_type = Column(String)

    description = Column(String)

    issue_date = Column(Date)
    expiration_date = Column(Date)

    status = Column(String)

    last_contact_date = Column(Date)

    renewed = Column(Integer, default=0)