from api.services.rest_client import RestClient
from api.services.router import Router
from api.models.requests.user import User


class Users:

    @staticmethod
    def create_session(session):
        url = Router.get_url(Router.USER_SERVICES, Router.SESSIONS)
        response =  RestClient.post(url, session.dict())
        if response["message"] == "session created":
            url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.USER_STATUS)
            user = User(email=session.email)
            RestClient.post(url, user.dict())
        return response
