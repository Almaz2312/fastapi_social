import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path('.') / '.envs' / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = 'Dweeter'
    PROJECT_VERSION: str = '1.0.0'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    TEST_USER_EMAIL = 'test@example.com'


settings = Settings()
