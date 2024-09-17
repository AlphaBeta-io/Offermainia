import re
import uuid
from fastapi import APIRouter, Depends, status, HTTPException, Response
from app import database #check line 10 
from .... import schemas, utils
from psycopg2 import sql

router = APIRouter(
    prefix= "/register",
    tags = ['Auth']
)


@router.post('/admin')
def register(user_details: schemas.UserRegisterDetails):
    try:
        cursor, conn = database.connection()
        query = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s)").format(sql.Identifier('admin_user'))
        cursor.execute(query, (str(uuid.uuid4()), user_details.email,utils.hash_password(user_details.password),))
        conn.commit()
        return {"message": "Successfully Registered "}
    except Exception as e:
        return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= f"Internal Server Error: {e}")
    finally:
        cursor.close()
        conn.close()