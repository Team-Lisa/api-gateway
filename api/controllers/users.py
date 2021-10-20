from api.services.rest_client import RestClient
from api.services.router import Router


class Users:

    @staticmethod
    def create_session(session):
        url = Router.get_url(Router.USER_SERVICES, Router.SESSIONS)
        return RestClient.post(url, session.dict())
