from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    database_host: str
    database_name: str 
    database_pass: str
    database_user: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


settings = Settings()