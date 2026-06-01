from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.schemas.action import ActionRequest
from app.schemas.renew import RenewRequest

from app.services.policy_service import (
    get_policies,
    create_action,
    renew_policy
)

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



@router.get("/policies")
def list_policies(
    status: str = None,
    db: Session = Depends(get_db)
):

    return get_policies(
        db,
        status
    )

@router.post("/policies/{policy_id}/actions")
def add_action(
    policy_id: int,
    payload: ActionRequest,
    db: Session = Depends(get_db)
):

    return create_action(
        db,
        policy_id,
        payload.notes
    )


@router.post("/policies/{policy_id}/renew")
def renew(
    policy_id: int,
    payload: RenewRequest,
    db: Session = Depends(get_db)
):

    policy = renew_policy(
        db,
        policy_id,
        payload.new_expiration_date
    )

    if not policy:
        return {
            "message": "Policy not found"
        }

    return {
        "message": "Policy renewed successfully",
        "policy_id": policy.id
    }

