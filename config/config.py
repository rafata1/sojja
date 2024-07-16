import os

from dotenv import load_dotenv

load_dotenv()

APP_PORT = int(os.getenv("APP_PORT", 8000))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
MONGO_USERNAME = os.getenv('MONGO_USERNAME', 'root')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', '1')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'optiwrite')
