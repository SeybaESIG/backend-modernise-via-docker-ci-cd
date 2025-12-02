from fastapi import FastAPI

app = FastAPI(title="Modernized API")


@app.get("/health")
def health_check():
    """Simple health endpoint."""
    return {"status": "ok"}

