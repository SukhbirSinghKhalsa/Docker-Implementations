from fastapi import FastAPI
from routes.user_routes import router
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="User Service")
app.include_router(router, prefix="/users")
