from api.services.rest_client import RestClient
from api.services.router import Router


class Gamification:

    @staticmethod
    def get_user_status(email):
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.USER_STATUS, params={"email":email})
        return RestClient.get(url)

    @staticmethod
    def get_trohpies():
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.TROPHIES)
        return RestClient.get(url)

    @staticmethod
    def update_user_points(email, points):
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.POINTS,params={"email":email})
        points = {"points": points}
        return RestClient.patch(url, points)

    @staticmethod
    def update_user_minutes(email, minutes):
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.MINUTES,params={"email":email})
        return RestClient.patch(url, minutes.dict())

    @staticmethod
    def update_user_lives(email, lives):
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.LIVES, params={"email":email})
        return RestClient.patch(url, lives.dict())

    @staticmethod
    def update_user_fastforwards(email, amount):
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.FASTFORWARDS,params= {"email":email})
        return RestClient.patch(url, amount.dict())

    @staticmethod
    def update_history_lesson(challenge_id, unit_id, lesson_id, email,allExercises):
        json = {"lesonIdCompleted":lesson_id,
                "allExercisesLesson":allExercises}
        url = Router.get_url(Router.GAMIFICATION_SERVICES,Router.HISTORY,challenge_id,unit_id,{"email":email})
        return RestClient.patch(url, json)

    @staticmethod
    def update_history_exam(challenge_id, unit_id, email,points):
        json = {"examCompleted": True,
                "allExercisesExam": points.allExercisesExam,
                "time": points.time,
                "unitCompleted": points.unitCompleted}
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.HISTORY, challenge_id, unit_id, {"email": email})
        return RestClient.patch(url, json)

    @staticmethod
    def update_challenge_completed(challenge_id, email):
        json = ""
        url = Router.get_url(Router.GAMIFICATION_SERVICES, Router.CHALLENGE_COMPLETED, id_1=challenge_id, params={"email": email})
        return RestClient.patch(url, json)






