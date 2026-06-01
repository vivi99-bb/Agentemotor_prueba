from datetime import date

from app.models.policy import Policy
from app.models.policy_action import PolicyAction


def calculate_status(expiration_date, renewed=False):

    if renewed:
        return "renewed"

    today = date.today()

    days = (expiration_date - today).days

    if days >= 0:
        return "upcoming"

    if abs(days) <= 30:
        return "renewable"

    return "lost"

#obtener las polizas 
 
def get_policies(db, status=None):

    policies = db.query(Policy).all()

    result = []

    for policy in policies:

        current_status = calculate_status(
            policy.expiration_date,
            policy.renewed
        )

        if status and current_status != status:
            continue

        result.append({
            "id": policy.id,
            "client_id": policy.client_id,
            "policy_number": policy.policy_number,
            "policy_type": policy.policy_type,
            "expiration_date": policy.expiration_date,
            "status": current_status,
            "renewed": policy.renewed
        })

    return result


#crear la gestión de las acciones de las polizas
def create_action(
    db,
    policy_id,
    notes
):

    action = PolicyAction(
        id_policy=policy_id,
        action_date=date.today(),
        notes=notes
    )

    db.add(action)
    db.commit()
    db.refresh(action)

    return action



#renovar la poliza
def renew_policy(
    db,
    policy_id,
    new_expiration_date
):

    policy = (
        db.query(Policy)
        .filter(Policy.id == policy_id)
        .first()
    )

    if not policy:
        return None

    policy.expiration_date = new_expiration_date
    policy.renewed = True
    policy.status = "renewed"

    db.commit()
    db.refresh(policy)

    return policy
