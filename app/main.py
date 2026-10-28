from fastapi import FastAPI

app = FastAPI(
    title="Reliable API",
    description="A small service for practicing CI, containers, and reliability engineering.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"service": "reliable-api", "status": "running"}


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy"}
