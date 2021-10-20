from api.services.router import Router


def test_users_router():
    assert Router.USER_SERVICES in Router.SERVICES_INFORMATION
    url = Router.SERVICES_INFORMATION[Router.USER_SERVICES].get("BASE_URL")
    assert url is not None
