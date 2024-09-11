import time
from fastapi import FastAPI
from app import models
from app.router.authorization.admin_auth import register, login
import psycopg2
from .config import settings

app = FastAPI()


app.include_router(login.router)

app.include_router(register.router)