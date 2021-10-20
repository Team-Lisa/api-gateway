import os


class Router:
    EXERCISES_SERVICE = "EXERCISE_SERVICE"
    TEST_URL = "http://test.com"
    BASE_URL = "BASE_URL"
    CHALLENGES = "challenges"
    LESSONS = "lessons"
    SERVICES_INFORMATION={
        EXERCISES_SERVICE: {
            BASE_URL: os.getenv("EXERCISE_BASE_URL", TEST_URL),
            CHALLENGES: "challenges",
            LESSONS: "lessons/{}/exercises"
        }
    }


    @staticmethod
    def get_url(service_name, resource, id=None):
        base_url = Router.SERVICES_INFORMATION[service_name].get(Router.BASE_URL)
        endpoint = Router.SERVICES_INFORMATION[service_name].get(resource)

        if id is not None:
            endpoint = endpoint.format(id)

        return "{}/{}".format(base_url, endpoint)
