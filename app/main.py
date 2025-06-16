from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Git-to-Blog API is running 🚀"}
