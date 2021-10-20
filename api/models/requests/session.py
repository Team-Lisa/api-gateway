from pydantic.main import BaseModel


class Session(BaseModel):
    name: str
    email: str
    expo_token: str
