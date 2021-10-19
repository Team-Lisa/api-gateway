from fastapi import APIRouter

from api.controllers.exercises import Exercises

router = APIRouter(tags=["Exercises"])


@router.get("/challenges")
async def get_challenges():
    response = Exercises.get_challenges()
    return response.json()




