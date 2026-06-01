from app.database.connection import engine, Base

from app.models.client import Client
from app.models.policy import Policy
from app.models.policy_action import PolicyAction


def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Tablas creadas ✅")