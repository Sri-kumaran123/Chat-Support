import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    REFRESH_SECRET_KEY= os.getenv('REFRESH_KEY')
    JWT_SECRET_KEY =os.getenv('ACCESS_KEY')
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = 900       # 15 minutes
    JWT_REFRESH_TOKEN_EXPIRES = 604800   # 7 days