from fastapi import FastAPI
from app.routers import authent,documents

app = FastAPI()

app.include_router(authent.router)
app.include_router(documents.router)


@app.get("/")
def root():
    return {"message": "secure-ai-study-assistant API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}