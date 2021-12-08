from api.services.rest_client import RestClient
from api.services.router import Router


class Metrics:
    @staticmethod
    def get(from_date, to_date):
        params = {
            "from_date": from_date,
            "to_date": to_date
        }

        url = Router.get_url(Router.METRICS_SERVICE, Router.METRICS, params=params)
        return RestClient.get(url)