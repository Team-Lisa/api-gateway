from fastapi import APIRouter
from api.controllers.tracks import Tracks
from api.models.responses.metrics import Metrics
from api.controllers.metrics import Metrics as MetricsController

router = APIRouter(tags=["Tracks"])


@router.get("/metrics", status_code=200, response_model=Metrics)
async def create_track(from_date: str = "", to_date: str = ""):
    return MetricsController.get(from_date, to_date)

