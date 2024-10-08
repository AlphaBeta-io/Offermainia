
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv


SQLALCHEMY_DATABASE_URL = "postgresql://shrinit:Simba1805@offerlicious.postgres.database.azure.com/postgres" #"postgresql://<username>:<password>@<ip-address>/<hostname>/<database_name>"

engine = create_engine(SQLALCHEMY_DATABASE_URL) #engine is what is responsible for sql alchemy to connect to postgres database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def connection():
    try:
        print(33232432123)
        print(settings.database_host, settings.database_name, settings.database_user, settings.database_pass)   

        conn = psycopg2.connect(host= settings.database_host,database = settings.database_name, user= settings.database_user,password =settings.database_pass, cursor_factory= RealDictCursor)                             #(host, database, user, password)
        cursor = conn.cursor()
        print('the database connection was sucessfull')
        return cursor, conn
    except Exception as error:
        return {'error': error},{'error': error}
        print(f'error:{error}')