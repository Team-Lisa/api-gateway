from api.controllers.exercises import Exercises
import requests_mock

from api.services.router import Router


def test_get_all_exercises():
    url = Router.get_url(Router.EXERCISES_SERVICE, "challenges")

    with requests_mock.Mocker() as m:
        json = {"challenges": []}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_challenges()

        assert response.status_code == 200
        assert response.json() == json
