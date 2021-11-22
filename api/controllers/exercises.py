from api.services.rest_client import RestClient
from api.services.router import Router


class Exercises:

    @staticmethod
    def get_challenges(published=None):
        params = {}

        if published is not None:
            params = {"published": published}

        url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGES, params=params)
        return RestClient.get(url)
    
    @staticmethod
    def get_lesson_exercises(lesson_id):
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.LESSONS, lesson_id)
        return RestClient.get(url)

    @staticmethod
    def get_exam_exercises(exam_id):
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.EXAMS, exam_id)
        return RestClient.get(url)