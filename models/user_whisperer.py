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


def account_sign_in(accName, pword):
    user_db_session = sessionmaker(bind=engine)
    session = user_db_session()
    q = None
    if '@' in accName:
        email = accName
        q = session.query(User).filter_by(user_email=email).filter_by(user_pword=pword).first()
    else:
        name = accName
        q = session.query(User).filter_by(user_name=name).filter_by(user_pword=pword).first()

    if q is not None:
        session.close()
        return True
    else:
        session.close()
        return False


def user_query(data, opt=0):
    user_db_session = sessionmaker(bind=engine)
    session = user_db_session()
    q = None
    if opt is 0: q = session.query(User).filter_by(user_id=data).first()
    if opt is 1: q = session.query(User).filter_by(user_name=data).first()
    if opt is 2: q = session.query(User).filter_by(user_email=data).first()
    if opt is 3: q = session.query(User).filter_by(user_pword=data).first()
    session.close()
    return q

