import uvicorn
from fastapi import FastAPI
from api.routes import helpers, exercises, users, gamification, tracks

app = FastAPI()


app.include_router(helpers.router)
app.include_router(exercises.router)
app.include_router(users.router)
app.include_router(gamification.router)
app.include_router(tracks.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, log_level="info")