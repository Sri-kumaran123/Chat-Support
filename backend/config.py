import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    REFRESH_SECRET_KEY= os.getenv('REFRESH_KEY')
    ACCESS_SECRET_KEY=os.getenv('ACCESS_KEY')
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False