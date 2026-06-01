from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.connection import Base

class PolicyAction(Base):
    __tablename__ = "policy_actions"

    id = Column(Integer, primary_key=True, index=True)

    policy_id = Column(Integer, ForeignKey("policies.id"))

    action_date = Column(Date)

    notes = Column(String)