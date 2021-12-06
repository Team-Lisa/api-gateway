from api.services.rest_client import RestClient
from api.services.router import Router
from api.models.requests.user import User


class Tracks:

    @staticmethod
    def create_track(track):
        url = Router.get_url(Router.METRICS_SERVICE, Router.TRACKS)
        response = RestClient.post(url, track.dict())
        return response
