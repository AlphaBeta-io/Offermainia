from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


from sqlalchemy import Column, String, BigInteger, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AdminUser(Base):
    __tablename__ = 'admin_user'  # Fixed the table name convention
    id = Column(String, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(BigInteger, server_default=text("EXTRACT(EPOCH FROM NOW())::BIGINT"), nullable=False)


class CustomerUser(Base):
    __tablename__ = 'customer_user'  # Fixed the table name convention
    id = Column(String, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(BigInteger, server_default=text("EXTRACT(EPOCH FROM NOW())::BIGINT"), nullable=False)


class MerchantUser(Base):
    __tablename__ = 'merchant_user'  # Fixed the table name convention
    id = Column(String, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(BigInteger, server_default=text("EXTRACT(EPOCH FROM NOW())::BIGINT"), nullable=False)

