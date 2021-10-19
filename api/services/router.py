import os


class Router:
    EXERCISES_SERVICE = "EXERCISE_SERVICE"
    TEST_URL = "http://test.com"
    SERVICES_INFORMATION={
        EXERCISES_SERVICE: {
            "BASE_URL": os.getenv("EXERCISE_BASE_URL", TEST_URL)
        }
    }


    @staticmethod
    def get_url(service_name, resource):
        base_url = Router.SERVICES_INFORMATION[service_name].get("BASE_URL")
        return "{}/{}".format(base_url, resource)
