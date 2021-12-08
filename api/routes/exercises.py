from fastapi import APIRouter

from api.controllers.exercises import Exercises
from api.models.requests.challenge import Challenge
from api.models.requests.exercise import Exercise
from api.models.responses.challenges import Challenges
from api.models.responses.exercises import Exercises as ExercisesResponse

router = APIRouter(tags=["Exercises"])

@router.post("/challenges", status_code=201)
async def create(challenge: Challenge):
    return Exercises.create_challenge(challenge)

@router.post("/exercises", status_code=201)
async def create(exercise: Exercise):
    return Exercises.create_exercise(exercise)

@router.post("/challenges/{challenge_id}", status_code=201)
async def edit_challenge(challenge_id: str, challenge: Challenge):
    return Exercises.update_challenge(challenge_id, challenge)

@router.post("/exercises/{exercise_id}", status_code=201)
async def edit_exercise(exercise_id: str, exercise: Exercise):
    return Exercises.update_exercise(exercise_id, exercise)

@router.get("/challenges", response_model=Challenges)
async def get_challenges(published: str = None):
    return Exercises.get_challenges(published)

@router.get("/challenges/next")
async def get_next_challenge_id():
    return Exercises.get_next_challenge_id()

@router.get("/lessons/{lesson_id}/exercises", response_model=ExercisesResponse)
async def get_exercises_by_lesson_id(lesson_id: str):
    return Exercises.get_lesson_exercises(lesson_id)


@router.get("/exams/{exam_id}/exercises", response_model=ExercisesResponse)
async def get_exercises_by_lesson_id(exam_id: str):
    return Exercises.get_exam_exercises(exam_id)

@router.get("/exercises/next")
async def get_next_exercise_id():
    return Exercises.get_next_exercise_id()
