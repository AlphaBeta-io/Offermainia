import time
from fastapi import FastAPI
from app import models
from app.router import login, register
import psycopg2
from .config import settings

app = FastAPI()


app.include_router(login.router)

app.include_router(register.router)