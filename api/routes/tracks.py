from fastapi import APIRouter
from api.controllers.tracks import Tracks
from api.models.requests.tracks import Track
from api.models.responses.tracks import Track as TrackResponse

router = APIRouter(tags=["Tracks"])


@router.post("/tracks", status_code=201, response_model=TrackResponse)
async def create_track(track: Track):
    return Tracks.create_track(track)

