from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "RAG CI/CD API is running"}


@app.get("/health")
def health():
    return {"status": "healthy-v2"}
