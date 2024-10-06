import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    API_URL = os.getenv("MODEL")
    APIKEY = os.getenv('key')

    if API_KEY is None:
        raise ValueError("API_KEY not found in .env file")
    if API_URL is None:
        raise ValueError("API_URL not found in .env file")
