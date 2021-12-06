from api.models.responses.tracks import Track


def test_track_response():
    response = Track(message="track saved")
    assert response.message == "track saved"
