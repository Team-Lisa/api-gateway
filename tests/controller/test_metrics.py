import requests_mock

from api.controllers.metrics import Metrics
from api.services.router import Router


def test_get_lesson_exercises():
    from_date = "2022/10/11"
    to_date = "2022/11/12"
    url = Router.get_url(Router.METRICS_SERVICE, Router.METRICS, params={
        "from_date": from_date,
        "to_date": to_date
    })

    with requests_mock.Mocker() as m:
        json = {
          "metrics": {
            "new_access": [
              {
                "date": "2021/12/07",
                "access_amount": 6
              },
              {
                "date": "2021/12/08",
                "access_amount": 2
              }
            ],
            "unit_completed": [
              {
                "date": "2021/12/07",
                "units_completed_amount": 1
              }
            ],
            "exam_resolution_time": {
              "time": 9
            },
            "user_frequency": {
              "time": 13.5
            }
          }
        }
        m.register_uri('GET', url, json=json, status_code=200)
        response = Metrics.get(from_date, to_date)

        assert response == json