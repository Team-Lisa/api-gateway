from typing import List

from pydantic import BaseModel


class Exercise(BaseModel):
    lesson_id: str
    exercise_type: str
    question: str
    options: list
    correct_answer: str
    exercise_id: str

class Exercises(BaseModel):
    exercises: List[Exercise]