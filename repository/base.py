from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.po.base import Base

default_engine = create_engine("sqlite:///data.db?check_same_thread=False", echo=True)
Session = sessionmaker(bind=default_engine)
Base.metadata.create_all(default_engine, checkfirst=True)
