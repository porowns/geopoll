from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence

engine = create_engine('sqlite:///geo_user.db', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    user_name = Column(String(50))
    user_email = Column(String)
    user_pword = Column(String(12))


Base.metadata.create_all(engine)
