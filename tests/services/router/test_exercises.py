from api.services.router import Router


def test_exercise_router():
    assert Router.EXERCISES_SERVICE in Router.SERVICES_INFORMATION
    url = Router.SERVICES_INFORMATION[Router.EXERCISES_SERVICE].get("BASE_URL")
    assert url is not None
