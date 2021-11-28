from fastapi import APIRouter
from api.models.responses.message import Message
from api.controllers.gamification import Gamification
from api.models.responses.user import UserStatus as UserStatusResponse
from api.models.responses.trophies import Trophies as TrophiesResponse
from api.models.responses.points import Points as PointsResponse
from api.models.requests.points import Points as PointsRequest
from api.models.requests.minutes import Minutes as MinutesRequest
from api.models.responses.minutes import Minutes as MinutesResponse
from api.models.requests.lives import Lives as LivesRequest
from api.models.responses.lives import Lives as LivesResponse
from api.models.requests.fastforwards import Fastforwards as FastforwardsRequest
from api.models.responses.fastforwards import Fastforwards as FastforwardsResponse
from api.models.responses.wonTrophies import WonTrophies

router = APIRouter(tags=["Gamification"])

@router.get("/users/userstatus", status_code=201, response_model=UserStatusResponse)
async def get_user_status(email: str = ""):
    return Gamification.get_user_status(email)


@router.get("/trophies", status_code=201)
async def get_trophies():
    return Gamification.get_trohpies()


@router.patch("/points", response_model=PointsResponse)
async def update_user_points(points: PointsRequest,email: str = ""):
    return Gamification.update_user_points(email,points)


@router.patch("/minutes", response_model=WonTrophies)
async def update_user_minutes(minutes: MinutesRequest,email: str = ""):
    return Gamification.update_user_minutes(email,minutes)


@router.patch("/lives", response_model=LivesResponse)
async def update_user_lives(lives: LivesRequest,email: str = ""):
    return Gamification.update_user_lives(email,lives)


@router.patch("/fastforwards", response_model=WonTrophies)
async def update_user_fastforwards(amount: FastforwardsRequest,email: str = ""):
    return Gamification.update_user_fastforwards(email,amount)

@router.patch("/challenges/{challenge_id}/units/{unit_id}/lessons/{lesson_id}/results", response_model=WonTrophies)
async def update_history_lesson(points: PointsRequest, challenge_id: str, unit_id: str, lesson_id: str, email: str = ""):
    Gamification.update_history_lesson(challenge_id, unit_id, lesson_id, email)
    return Gamification.update_user_points(email, points)

@router.patch("/challenges/{challenge_id}/units/{unit_id}/exam",response_model=WonTrophies)
async def update_history_exam(points: PointsRequest, challenge_id: str, unit_id: str, email: str = ""):
    Gamification.update_history_exam(challenge_id, unit_id, email)
    return Gamification.update_user_points(email, points)

@router.patch("/challenges/{challenge_id}", response_model=WonTrophies)
async def update_challenge_completed( challenge_id: str, email: str = ""):
    return Gamification.update_challenge_completed(challenge_id,email)





