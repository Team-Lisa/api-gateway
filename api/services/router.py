import os


class Router:
    EXERCISES_SERVICE = "EXERCISE_SERVICE"
    USER_SERVICES = "USER_SERVICE"
    GAMIFICATION_SERVICES = "GAMIFICATION_SERVICE"
    TEST_URL = "http://test.com/"
    BASE_URL = "BASE_URL"
    CHALLENGES = "challenges"
    LESSONS = "lessons"
    SESSIONS = "sessions"
    EXAMS = "exams"
    USER_STATUS = "user_status"
    TROPHIES = "trophies"
    STOREITEMS = "storeitems"
    POINTS = "points"
    MINUTES = "minutes"
    LIVES = "lives"
    FASTFORWARDS = "fastforwards"
    HISTORY = "history"
    CHALLENGE_COMPLETED = "challenge_completed"
    USER_TROHPIES = "user_trophies"
    EXERCISE_NEXT_ID = "exercise_next_id"
    CHALLENGE_NEXT_ID = "challenge_next_id"
    SERVICES_INFORMATION = {
        EXERCISES_SERVICE: {
            BASE_URL: os.getenv("EXERCISES_BASE_URL", TEST_URL),
            CHALLENGES: "challenges",
            LESSONS: "lessons/{}/exercises",
            EXAMS: "exams/{}/exercises",
            EXERCISE_NEXT_ID: "exercises/next",
            CHALLENGE_NEXT_ID: "challenges/next"
        },
        USER_SERVICES: {
            BASE_URL: os.getenv("USERS_BASE_URL", TEST_URL),
            SESSIONS: "users/sessions"
        },
        GAMIFICATION_SERVICES: {
            BASE_URL: os.getenv("GAMIFICATIONS_BASE_URL", TEST_URL),
            USER_STATUS: "users",
            TROPHIES:"trophies",
            USER_TROHPIES:"users/trophies",
            STOREITEMS:"storeitems",
            POINTS: "points",
            MINUTES: "minutes",
            LIVES: "lives",
            FASTFORWARDS: "fastforwards",
            HISTORY: "users/history/challenges/{}/units/{}",
            CHALLENGE_COMPLETED:"users/history/challenges/{}"

        }
    }


    @staticmethod
    def get_url(service_name, resource, id_1=None, id_2=None, params = {}):
        base_url = Router.SERVICES_INFORMATION[service_name].get(Router.BASE_URL)
        endpoint = Router.SERVICES_INFORMATION[service_name].get(resource)
        queryparams = "?"
        if len(params) > 0:
            for param in params:
                queryparams += param + "={}&".format(params[param])
            queryparams = queryparams[:len(queryparams)-1]
        else:
            queryparams = ""
        if id_1 is not None and id_1 is not None:
            endpoint = endpoint.format(id_1,id_2)
        elif id_1 is not None and id_2 is None:
            endpoint = endpoint.format(id_1)

        return "{}{}{}".format(base_url, endpoint, queryparams)
