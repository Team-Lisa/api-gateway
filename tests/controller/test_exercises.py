from api.controllers.exercises import Exercises
import requests_mock

from api.services.router import Router


def test_get_all_exercises():
    url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGES)

    with requests_mock.Mocker() as m:
        json = {"challenges": []}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_challenges()

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