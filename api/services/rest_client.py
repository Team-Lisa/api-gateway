import requests


class RestClient:

    @staticmethod
    def get(url):
        return requests.get(url)
