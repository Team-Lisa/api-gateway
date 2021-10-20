from api.services.rest_client import RestClient
from api.services.router import Router


class Exercises:

    @staticmethod
    def get_challenges():
        url = Router.get_url(Router.EXERCISES_SERVICE, "challenges")
        return RestClient.get(url)

    @staticmethod
    def get_lesson_exercises(lesson_id):
        url = Router.get_url(Router.EXERCISES_SERVICE, "lessons", lesson_id)
        return RestClient.get(url)