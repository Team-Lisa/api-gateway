
from api.models.responses.challenges import Challenges
from api.models.responses.exercises import Exercises


def test_challenges_response():
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = {
        "id": "1",
        "duration": 3600
    }
    lessons_1 = [
        {"name": "lesson_1",
         "id": "C1U1L1"},
        {"name": "lesson_2",
         "id": "C1U1L2"}
    ]

    units = [
        {"name": name_lesson_1,
         "exam": exam_1,
         "lessons": lessons_1,
         "id": "1"}
    ]
    challenge_id = "D1"
    challenge = {
        "challenge_id": challenge_id,
        "units": units,
        "name": name
    }

    response = Challenges(
        challenges=[challenge]
    )

    assert len(response.challenges) == 1


def test_exercises_response():
    exercise_type = "listening"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    exercise_id = "e1"
    lesson_id = "l1"
    exercise = {
        "exercise_type": exercise_type,
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "exercise_id": exercise_id,
        "lesson_id": lesson_id
    }
    response = Exercises(
        exercises=[exercise]
    )

    assert len(response.exercises) == 1