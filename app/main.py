from fastapi import FastAPI

from app.api import router

app = FastAPI(title="EV Purchase Prediction API")
app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "ok"}
