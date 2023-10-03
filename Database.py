from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_Database = "mysql+pymysql://root:harimonic123@localhost:3306/foxit"

engine = create_engine(URL_Database)

SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)

Base = declarative_base()