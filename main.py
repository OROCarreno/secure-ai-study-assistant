from fastapi import FastAPI
from backend import authent

app = FastAPI()

app.include_router(authent.router)


@app.get("/")
def root():
    return {"message": "secure-ai-study-assistant API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}