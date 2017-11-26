from sqlalchemy.orm import sessionmaker
from app import db, models
from app.models.table_declaration import User


def insert_new_user(name, email, pword):
    # create new user
    new_user = User(user_name=name, user_email =email, user_pword=pword)
    # add to the db
    db.session.add(new_user)
    db.session.commit()
    db.session.close()


def account_sign_in(accName, pword):
    q = None
    if '@' in accName:
        email = accName
        q = db.session.query(User).filter_by(user_email=email).filter_by(user_pword=pword).first()
    else:
        name = accName
        q = db.session.query(User).filter_by(user_name=name).filter_by(user_pword=pword).first()
    db.session.close()
    return q


def user_query(data, opt=0):
    q = None
    if opt is 0: q = db.session.query(User).filter_by(user_id=data).first()
    if opt is 1: q = db.session.query(User).filter_by(user_name=data).first()
    if opt is 2: q = db.session.query(User).filter_by(user_email=data).first()
    if opt is 3: q = db.session.query(User).filter_by(user_pword=data).first()
    db.session.close()
    return q
