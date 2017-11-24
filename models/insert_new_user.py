import sqlalchemy
from jinja2 import meta
from sqlalchemy.orm import sessionmaker, session
from models.table_declaration import User, engine, inspect, Table


def insert_new_user(name, email, pword):
    # connect to geo_user table
    user_db_session = sessionmaker(bind=engine)
    session = user_db_session()
    # insert user
    new_user = User(user_name=name, user_email =email, user_pword=pword)
    session.add(new_user)
    session.commit()

    # view contents of table
    #instances = session.query(User).all()
    #for i in instances:
    #    print(i.user_name,i.user_email,i.user_pword)

    session.close()