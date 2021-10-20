import os


class Router:
    EXERCISES_SERVICE = "EXERCISE_SERVICE"
    USER_SERVICES = "USER_SERVICE"
    TEST_URL = "http://test.com"
    BASE_URL = "BASE_URL"
    CHALLENGES = "challenges"
    LESSONS = "lessons"
    SESSIONS = "sessions"
    EXAMS = "exams"
    SERVICES_INFORMATION = {
        EXERCISES_SERVICE: {
            BASE_URL: os.getenv("EXERCISE_BASE_URL", TEST_URL),
            CHALLENGES: "challenges",
            LESSONS: "lessons/{}/exercises",
            EXAMS: "exams/{}/exercises"
        },
        USER_SERVICES: {
            BASE_URL: os.getenv("USER_BASE_URL", TEST_URL),
            SESSIONS: "sessions"
        }
    }


    @staticmethod
    def get_url(service_name, resource, id=None):
        base_url = Router.SERVICES_INFORMATION[service_name].get(Router.BASE_URL)
        endpoint = Router.SERVICES_INFORMATION[service_name].get(resource)

        if id is not None:
            endpoint = endpoint.format(id)

        return "{}/{}".format(base_url, endpoint)
