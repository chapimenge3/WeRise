from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.settings import settings

# Get the database connection information from the environment variables
DB_NAME = settings.DB_NAME
USER = settings.DB_USER
PASSWORD = settings.DB_PASSWORD
HOST = settings.DB_HOST
PORT = settings.DB_PORT

# Create the database connection string
CONNECTION_STRING = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
# Create the database engine
engine = create_engine(CONNECTION_STRING)
session = Session(engine)