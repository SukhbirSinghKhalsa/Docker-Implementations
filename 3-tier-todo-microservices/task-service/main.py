from fastapi import FastAPI
from routes.task_routes import router
from database import engine, Base
import logging

logging.basicConfig(level=logging.INFO)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Service")
app.include_router(router, prefix="/tasks")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
