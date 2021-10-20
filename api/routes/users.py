from fastapi import APIRouter

from api.controllers.users import Users
from api.models.requests.session import Session
from api.models.responses.message import Message

router = APIRouter(tags=["Users"])


@router.post("/sessions", status_code=201, response_model=Message)
async def create_session(session: Session):
    return Users.create_session(session)




