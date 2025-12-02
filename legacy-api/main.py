from fastapi import FastAPI

app = FastAPI(title="Legacy API")


@app.get("/health")
def health_check():
    return {"status": "ok"}

