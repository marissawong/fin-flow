from dotenv import load_dotenv
from fastapi import FastAPI

from app.presentation.api import user_routes

load_dotenv()

app = FastAPI(title="FinFlow")

app.include_router(user_routes.router, prefix="/api")