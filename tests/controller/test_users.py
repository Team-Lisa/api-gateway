import requests_mock

from api.controllers.users import Users
from api.models.requests.session import Session
from api.services.router import Router


def test_create_session():
    url = Router.get_url(Router.USER_SERVICES, Router.SESSIONS)
    create_user_status_url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.USER_STATUS)
    session = Session(
        name="name lastname",
        email="fake@fi.uba.ar",
        expo_token="fake_token"
    )
    with requests_mock.Mocker() as m:
        json = {"message": "session created"}
        m.register_uri('POST', create_user_status_url, json=json, status_code=201)
        m.register_uri('POST', url, json=json, status_code=201)
        response = Users.create_session(session)

        assert response == json