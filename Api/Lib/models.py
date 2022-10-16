import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker,relationship # type: ignore
from sqlalchemy.sql import expression
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
from datetime import datetime

DB_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DB_URL)

SessionLocal = sessionmaker( bind=engine)
session=SessionLocal()
Base = declarative_base() 
Now = datetime.utcnow()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def db_reset():
    #Veritabanını sıfırlamak için hazırlan fonksiyon
   Base.metadata.reflect(bind=engine)
   Base.metadata.drop_all(bind=engine)
   


class İmages(Base):
    """Proje oluşturmamızı sağlayan Sınıf"""
    __tablename__ = "images"
    
    id = Column(Integer, primary_key=True)
    image_name = Column(String(100))
    created_at= Column(Date,default=Now)
    user_id=Column(Integer, ForeignKey("user.id"))

    def __init__(self, name):
     """ Dışardan gelen requestler için başlangıç fonksiyonu"""
     self.name = name
    
    



class Video(Base):
  """Proje oluşturmamızı sağlayan Sınıf """

  __tablename__ = "jobs"
  id = Column(Integer, primary_key=True)
  name =Column(String(80))
  created_at= Column(Date,default=Now)
  user_id=Column(Integer, ForeignKey("user.id"))

  



class User(Base):
    """ Kullanıcı oluşturmamızı sağlayan Sınıf """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), unique=True, nullable=False)


    def __init__(self, username,password):
     self.username =username
     self.password =password






db_reset()

Base.metadata.create_all(bind=engine)



new_user=User(username="admin",password="admin")

session.add_all([new_user ])

session.commit()
