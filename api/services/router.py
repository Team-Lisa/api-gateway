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
    SERVICES_INFORMATION = {
        EXERCISES_SERVICE: {
            BASE_URL: os.getenv("EXERCISES_BASE_URL", TEST_URL),
            CHALLENGES: "challenges",
            LESSONS: "lessons/{}/exercises",
            EXAMS: "exams/{}/exercises"
        },
        USER_SERVICES: {
            BASE_URL: os.getenv("USERS_BASE_URL", TEST_URL),
            SESSIONS: "users/sessions"
        },
        GAMIFICATION_SERVICES: {
            BASE_URL: os.getenv("GAMIFICATIONS_BASE_URL", TEST_URL),
            USER_STATUS: "users",
            TROPHIES:"trohpies",
            STOREITEMS:"storeitems",
            POINTS: "points",
            MINUTES: "minutes",
            LIVES: "lives",
            FASTFORWARDS: "fastforwards",
            HISTORY: "/users/history/challenges/{}/units/{}",
            CHALLENGE_COMPLETED:"/users/history/challenges/{}"

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
            queryparams = queryparams[:len(queryparams)-2]
        else:
            queryparams = ""
        if id is not None:
            endpoint = endpoint.format(id)

        return "{}{}".format(base_url, endpoint)
