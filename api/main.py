from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Cloud Lab 1")

@app.get("/")
@app.get("/api")
@app.api_route("/{path_name:path}", methods=["GET"])
def get_root(path_name: str = ""):
    return {
        "status": "success",
        "message": "Лабораторная работа №1 успешно развернута в Vercel!",
        "service": "PaaS / Serverless Web Service",
        "timestamp": datetime.utcnow().isoformat()
    }