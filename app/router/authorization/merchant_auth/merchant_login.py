from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ....oauth2 import oauth2_merchent #check line 10 
from .... import schemas, models, database, utils
from psycopg2 import sql

router = APIRouter(
    prefix= "/login",
    tags = ['Auth']
)

@router.post('/merchant')
def login(user_details: schemas.UserLoginDetails,):
    try:
        cursor, conn  = database.connection()
        query = sql.SQL("SELECT * FROM {} where email = %s").format(sql.Identifier('merchant_user'))
        cursor.execute(query, (user_details.email,))
        result = cursor.fetchone()
        result = dict(result)
        if not result:
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")
        if not utils.verify(user_details.password, result['password']):
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")
        access_token = oauth2_merchent.create_access_token(data = {"user_id":result['email']})
        conn.close()
        return Response({"access_token": access_token, "token_type": "bearer"}, status_code= status.HTTP_200_OK) 
    except Exception as e:
        return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}")
