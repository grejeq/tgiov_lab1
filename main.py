from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Lab 1")

@app.get("/")
def get_root():
    return {
        "status": "success",
        "message": "Лабораторная работа №1 успешно развернута в Render!",
        "service": "PaaS Web Service",
        "timestamp": datetime.utcnow().isoformat()
    }