from fastapi import FastAPI

from app.api.webhook import router as webhook_router

app = FastAPI()

app.include_router(webhook_router, prefix="/github")

@app.get("/")
def read_root():
    return {"message": "Git-to-Blog API is running 🚀"}
