# The smallest useful FastAPI app. Run with: uvicorn hello_api:app --reload

from fastapi import FastAPI

app = FastAPI(title="Hello DevOps API")


@app.get("/")
def hello():
    return {"message": "Hello Dosto, this is FastAPI!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
