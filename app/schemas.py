from csv import unregister_dialect
from typing import Optional
from xmlrpc.client import Boolean
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class UserLoginDetails(BaseModel):
    email: EmailStr
    password: str

class UserRegisterDetails(UserLoginDetails):
    confirm_password: str
    newsletter: Boolean