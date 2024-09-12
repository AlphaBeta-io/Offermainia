from logging.config import IDENTIFIER
import uuid
from xml.dom.minidom import Identified
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from app import database #check line 10 
from .... import schemas, utils
from psycopg2 import sql

router = APIRouter(
    prefix= "/register",
    tags = ['Auth']
)



@router.post('/merchant')
def register(user_details: schemas.UserRegisterDetails):
    try:
        cursor, conn = database.connection()
        query = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s)").format(sql.Identifier('merchant_user'))
        cursor.execute(query, (str(uuid.uuid4()), user_details.email,utils.hash_password(user_details.password),))
        conn.commit()
        return Response({"message": "Successfully Registered "}, status_code=status.HTTP_200_OK)
    except Exception as e:
        return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= f"Internal Server Error: {e}")
    finally:
        cursor.close()
        conn.close()
        