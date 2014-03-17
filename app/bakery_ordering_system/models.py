import config

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Text

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

engine = create_engine(config.DB_URI, echo=False) 
session = scoped_session(sessionmaker(bind=engine,
                         autocommit = False,
                         autoflush = False))

Base = declarative_base()
Base.query = session.query_property()


class Customer(Base):
    __tablename__= 'customers'
    id = Column(Integer, primary_key = True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    phonenumber = Column(String(20))
    email = Column(String(120), unique=True)

def create_tables():
    Base.metadata.create_all(engine)