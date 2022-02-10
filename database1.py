from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    database='fastapp',
                                    user='root',
                                    password='1234')
if connection.is_connected():
    db_info = connection.get_server_info()

# DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapp"

engine = create_engine(connection)

SessionLocal = sessionmaker(bind = engine, autocommit=False,autoflush= False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close