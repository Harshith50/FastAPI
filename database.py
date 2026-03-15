from sqlalchemy import create_engine;
from dotenv import load_dotenv;
import os;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus


load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
# Connection
engine = create_engine(DATABASE_URL)

# session
Sessionlocal = sessionmaker(autoflush=False , autocommit= False, bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally :
        db.close()    

# base
Base = declarative_base()