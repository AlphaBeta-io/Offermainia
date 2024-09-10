from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class AdminUser(Base):
    __tablename__= 'admin-user'
    id = Column(String,primary_key= True, nullable= False)
    email = Column(String, nullable= False, unique= True)
    password = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone= True), server_default = text('now()'), nullable= False) 
