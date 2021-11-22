from api.controllers.exercises import Exercises
import requests_mock

from api.services.router import Router


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
