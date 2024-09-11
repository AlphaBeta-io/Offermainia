from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ....oauth2 import oauth2_customers #check line 10 
from .... import schemas, models, database, utils
from psycopg2 import sql

cursor, conn  = database.connection()
router = APIRouter(
    prefix= "/login",
    tags = ['Auth']
)

@router.post('/customer')
def login(user_details: schemas.UserLoginDetails,):
    query = sql.SQL("SELECT * FROM {} where email = %s").format(sql.Identifier('customer_user'))
    cursor.execute(query, (user_details.email,))
    result = cursor.fetchone()
    print(result)
    result = dict(result)
    print(result)
    if not result:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")
    if not utils.verify(user_details.password, result['password']):
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")

    # create a token and return a token
    #pip install python-jose[cryptography]
    # go to ..oauth.py
    access_token = oauth2_customers.create_access_token(data = {"user_id":result['email']})
    conn.close()
    return {"access_token": access_token, "token_type": "bearer"}
