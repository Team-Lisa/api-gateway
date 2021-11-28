from api.services.rest_client import RestClient
from api.services.router import Router


class Exercises:

    @staticmethod
    def create_challenge(challenge):
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGES)
        return RestClient.post(url, challenge)

    @staticmethod
    def create_exercise(exercise):
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.EXERCISES)
        return RestClient.post(url, exercise)

    @staticmethod
    def update_challenge(challenge_id, challenge):
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.UPDATE_CHALLENGE, challenge_id)
        return RestClient.post(url, challenge)

    @staticmethod
    def update_exercise(exercise_id, exercise):
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.UPDATE_EXERCISE, exercise_id)
        return RestClient.post(url, exercise)

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

    @staticmethod
    def get_next_exercise_id():
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.EXERCISE_NEXT_ID)
        return RestClient.get(url)

    @staticmethod
    def get_next_challenge_id():
        url = Router.get_url(Router.EXERCISES_SERVICE, Router.CHALLENGE_NEXT_ID)
        return RestClient.get(url)