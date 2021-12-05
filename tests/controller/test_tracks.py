import requests_mock
from api.controllers.tracks import Tracks
from api.models.requests.tracks import Track as TrackModel
from api.services.router import Router


def test_create_session():
    url = Router.get_url(Router.METRICS_SERVICE, Router.TRACKS)
    track = TrackModel(
        name="new_access",
        event_data={},
        date="2021/11/11"
    )
    with requests_mock.Mocker() as m:
        json = {"message": "track saved"}
        m.register_uri('POST', url, json=json, status_code=201)

        response = Tracks.create_track(track)

        assert response == json