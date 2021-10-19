from api.services.rest_client import RestClient
from api.services.router import Router


class Exercises:

    @staticmethod
    def get_challenges():
        url = Router.get_url(Router.EXERCISES_SERVICE, "challenges")
        return RestClient.get(url)
