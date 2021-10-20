from api.models.responses.message import Message


def test_sessions_response():
    response = Message(message="session created")
    assert response.message == "session created"
