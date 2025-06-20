from fastapi import FastAPI
from mangum import Mangum

from app.api.webhook import router as webhook_router
from app.api.user import router as user_router
from app.api.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(webhook_router, prefix="/github")

@app.get("/")
def read_root():
    return {"message": "Git-to-Blog API is running."}

handler = Mangum(app,lifespan="auto")