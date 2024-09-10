import os
from fastapi import Depends, status, HTTPException
import jwt
from datetime import datetime, timedelta
from . import schemas, models, database
from fastapi.security import OAuth2PasswordBearer
from .config import settings
from psycopg2 import sql

cursor, conn = database.connection()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login/admin')
#SECRET_KEY = which resides on our server only

#Algorithm we want to use

#we need to give the expiration time

# to get a string like this run:
# openssl rand -hex 32

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+ timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id = id)
    except Exception as e:
        return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return token_data


#this functrions checks wether the user is 
def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail= f'Could not validate credentials', headers = {"WWW-Auhenticate": "Bearer"})
    token = verify_access_token(token, credentials_exception)
    # query = db.query(models.User).filter(models.User.id == token.id).first()
    query = sql.SQL("SELECT id FROM {} AS adu WHERE adu.id = token.id").format(sql.Identifier('admin-user'))
    cursor.execute(query)
    admin_user= cursor.fetchall()
    return admin_user