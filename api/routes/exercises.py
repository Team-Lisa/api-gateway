from fastapi import APIRouter

from api.controllers.exercises import Exercises

router = APIRouter(tags=["Exercises"])


@router.get("/challenges")
async def get_challenges():
    return Exercises.get_challenges()


@router.get("/lessons/{lesson_id}/exercises")
async def get_exercises_by_lesson_id(lesson_id: str):
    response = Exercises.get_lesson_exercises(lesson_id)
    return response.json()


