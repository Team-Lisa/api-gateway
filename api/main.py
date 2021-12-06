import uvicorn
from fastapi import FastAPI
from api.routes import helpers, exercises, users, gamification, tracks
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(helpers.router)
app.include_router(exercises.router)
app.include_router(users.router)
app.include_router(gamification.router)
app.include_router(tracks.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, log_level="info")