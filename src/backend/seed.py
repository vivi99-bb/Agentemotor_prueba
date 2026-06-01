from datetime import date, timedelta

from app.database.connection import SessionLocal
from app.models.client import Client
from app.models.policy import Policy
from app.models.policy_action import PolicyAction

db = SessionLocal()

client = [
    Client(name="Juan Pérez", email="juan@test.com", phone="3001115811", document="1001"),
    Client(name="María Gómez", email="maria@test.com", phone="3001946222", document="1002"),
    Client(name="Carlos Ruiz", email="carlos@test.com", phone="3003139433", document="1003"),
    Client(name="Ana López", email="ana@test.com", phone="3004875944", document="1004"),
    Client(name="Pedro Torres", email="pedro@test.com", phone="3005555855", document="1005"),
    Client(name="Laura Díaz", email="laura@test.com", phone="3006661686", document="1006"),
    Client(name="Jorge Castro", email="jorge@test.com", phone="3016485377", document="1007")
]

db.add_all(client)
db.commit()

for c in client:
    db.refresh(c)

today = date.today()

policy  = [

    # Próximas a vencer
    Policy(
        client_id=client[0].id,
        policy_number="POL-001",
        policy_type="Auto",
        description="Seguro automóvil Mazda",
        issue_date=today - timedelta(days=350),
        expiration_date=today + timedelta(days=15),
        status="upcoming",
        last_contact_date=today - timedelta(days=5),
        renewed=False
    ),

    Policy(
        client_id=client[1].id,
        policy_number="POL-002",
        policy_type="Vida",
        description="Seguro de vida",
        issue_date=today - timedelta(days=350),
        expiration_date=today + timedelta(days=5),
        status="upcoming",
        last_contact_date=today - timedelta(days=2),
        renewed=False
    ),

    # Vence hoy
    Policy(
        client_id=client[2].id,
        policy_number="POL-003",
        policy_type="Hogar",
        description="Seguro vivienda",
        issue_date=today - timedelta(days=365),
        expiration_date=today,
        status="upcoming",
        last_contact_date=today,
        renewed=False
    ),

    # Ventana crítica (<30 días)
    Policy(
        client_id=client[3].id,
        policy_number="POL-004",
        policy_type="Auto",
        description="Seguro automóvil Kia",
        issue_date=today - timedelta(days=365),
        expiration_date=today - timedelta(days=10),
        status="renewable",
        last_contact_date=today - timedelta(days=3),
        renewed=False
    ),

    Policy(
        client_id=client[4].id,
        policy_number="POL-005",
        policy_type="Vida",
        description="Seguro familiar",
        issue_date=today - timedelta(days=365),
        expiration_date=today - timedelta(days=25),
        status="renewable",
        last_contact_date=today - timedelta(days=7),
        renewed=False
    ),

    # Perdida (>30 días)
    Policy(
        client_id=client[5].id,
        policy_number="POL-006",
        policy_type="Hogar",
        description="Seguro apartamento",
        issue_date=today - timedelta(days=365),
        expiration_date=today - timedelta(days=45),
        status="lost",
        last_contact_date=today - timedelta(days=35),
        renewed=False
    ),

    # Renovada
    Policy(
        client_id=client[6].id,
        policy_number="POL-007",
        policy_type="Auto",
        description="Seguro automóvil Renault",
        issue_date=today - timedelta(days=30),
        expiration_date=today + timedelta(days=365),
        status="renewed",
        last_contact_date=today - timedelta(days=1),
        renewed=True
    )
]

db.add_all(policy)
db.commit()

actions = [
    PolicyAction(policy_id=policy[3].id, action_date=today - timedelta(days=9), notes="Primera llamada"),
    PolicyAction(policy_id=policy[3].id, action_date=today - timedelta(days=5), notes="Cliente interesado"),

    PolicyAction(policy_id=policy[4].id, action_date=today - timedelta(days=20), notes="Correo enviado"),
    PolicyAction(policy_id=policy[4].id, action_date=today - timedelta(days=15), notes="Seguimiento realizado"),

    PolicyAction(policy_id=policy[5].id, action_date=today - timedelta(days=40), notes="Sin respuesta"),
    PolicyAction(policy_id=policy[5].id, action_date=today - timedelta(days=38), notes="Segundo intento"),

    PolicyAction(policy_id=policy[6].id, action_date=today - timedelta(days=3), notes="Renovación aprobada"),

    PolicyAction(policy_id=policy[6].id, action_date=today - timedelta(days=1), notes="Recordatorio enviado"),

    PolicyAction(policy_id=policy[0].id, action_date=today - timedelta(days=2), notes="Primer contacto"),

    PolicyAction(policy_id=policy[1].id, action_date=today, notes="Llamada programada")
]

for action in actions:
    db.add_all([action])

db.commit()

print("Datos cargados")