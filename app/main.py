import time
from fastapi import FastAPI
from app import models
from app.router.authorization.admin_auth import register, login
from app.router.authorization.customer_auth import customer_register, customer_login
from app.router.authorization.merchant_auth import merchant_register, merchant_login
import psycopg2
from .config import settings

app = FastAPI()


app.include_router(login.router)

app.include_router(register.router)

app.include_router(customer_login.router)

app.include_router(customer_register.router)

app.include_router(merchant_login.router)

app.include_router(merchant_register.router)

