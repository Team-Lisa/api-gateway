from api.controllers.exercises import Exercises
import requests_mock

from api.services.router import Router
import json as JSON


def test_get_all_challenges():
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGES)

    with requests_mock.Mocker() as m:
        json = {"challenges": []}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_challenges()

        assert response == json

def test_get_all_challenges_published():
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGES, params={"published": "true"})

    with requests_mock.Mocker() as m:
        json = {"challenges": []}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_challenges(published="true")

        assert response == json

def test_get_all_challenges_not_published():
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGES, params={"published": "false"})

    with requests_mock.Mocker() as m:
        json = {"challenges": []}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_challenges(published="false")

        assert response == json

def test_get_lesson_exercises():
    lesson_id = "L1"
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.LESSONS, lesson_id)

    with requests_mock.Mocker() as m:
        json = {"lessons": []}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_lesson_exercises(lesson_id)

        assert response == json

def test_get_exam_exercises():
    exam_id = "E1"
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.EXAMS, exam_id)

    with requests_mock.Mocker() as m:
        json = {"lessons": []}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_exam_exercises(exam_id)

        assert response == json

def test_get_exercise_next_id():
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.EXERCISE_NEXT_ID)

    with requests_mock.Mocker() as m:
        json = {"next_exercise_id": "C1U1L1E2"}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_next_exercise_id()

        assert response == json

def test_get_challenge_next_id():
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGE_NEXT_ID)

    with requests_mock.Mocker() as m:
        json = {"next_challenge_id": "C1U1L1E2"}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_next_challenge_id()

        assert response == json

def test_create_exercise():
    exercise = {
        "lesson_id": "C1U1L1",
        "exercise_type": "TranslateToOriginal",
        "question": "question_2",
        "options": ["a", "b", "adddd"],
        "correct_answer": "a",
        "exercise_id": "C1U1L1E1"
    }
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.EXERCISES)

    with requests_mock.Mocker() as m:
        json = {"exercise": JSON.dumps(exercise)}
        m.register_uri('POST', url, json=json, status_code=201)
        response = Exercises.create_exercise(JSON.dumps(exercise))

        assert response == json

def test_create_challenge():
    challenge = {
        "name": "testiing2255",
        "units": [],
        "id": "C1",
        "published": False
    }
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGES)

    with requests_mock.Mocker() as m:
        json = {"challenge": JSON.dumps(challenge)}
        m.register_uri('POST', url, json=json, status_code=201)
        response = Exercises.create_challenge(JSON.dumps(challenge))

        assert response == json

def test_update_exercise():
    exercise_id = "C1U1L1E1"
    exercise = {
        "lesson_id": "C1U1L1",
        "exercise_type": "TranslateToOriginal",
        "question": "question_2",
        "options": ["a", "b", "adddd"],
        "correct_answer": "a",
        "exercise_id": "C1U1L1E1"
    }
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.UPDATE_EXERCISE, exercise_id)

    with requests_mock.Mocker() as m:
        json = {"exercise": JSON.dumps(exercise)}
        m.register_uri('POST', url, json=json, status_code=201)
        response = Exercises.update_exercise(exercise_id, JSON.dumps(exercise))

        assert response == json

def test_update_challenge():
    challenge_id = "C1"
    challenge = {
        "name": "testiing2255",
        "units": [],
        "id": "C1",
        "published": False
    }
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.UPDATE_CHALLENGE, challenge_id)

    with requests_mock.Mocker() as m:
        json = {"challenge": JSON.dumps(challenge)}
        m.register_uri('POST', url, json=json, status_code=201)
        response = Exercises.update_challenge(challenge_id, JSON.dumps(challenge))

        assert response == json