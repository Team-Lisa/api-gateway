from typing import Optional

from pydantic.main import BaseModel


class Points(BaseModel):
    points: int #un numero positivo sumara puntos, mientras que un numero negativo los restara
    allExercisesExam: Optional[bool] = None
    allExercisesLesson: Optional[bool] = None
    time: Optional[int] = None
    unitCompleted: Optional[bool] = None
