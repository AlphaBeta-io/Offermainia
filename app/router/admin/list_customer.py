from fastapi import APIRouter, Depends, status, HTTPException, Response

from ...oauth2 import oauth2_admin 
# from ...oauth2 import oauth2_customers #check line 10 
from ... import schemas, models, database, utils
from psycopg2 import sql


router = APIRouter(
    prefix= "/customer",
    tags = ['admin']
)

@router.get('/')
def list_customer(current_user: str = Depends(oauth2_admin.get_current_user)):
    try:
        cursor, conn  = database.connection()
        try:
            current_user_dict = dict(current_user[0])
            print(123123,current_user_dict)
            query= sql.SQL("SELECT * FROM {} where id = %s").format(sql.Identifier('admin_user'))
            cursor.execute(query, (current_user_dict['id'],))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials")
        except Exception as e:
            return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}")
        query = sql.SQL("SELECT * FROM {}").format(sql.Identifier('customer_user'))
        cursor.execute(query)
        result = cursor.fetchall()
        print(dict(result[0]))
        return result
    except Exception as e:
        return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}")