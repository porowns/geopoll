from sqlalchemy.orm import sessionmaker
from werkzeug.security import check_password_hash

from app import db, models
from app.models.table_declaration import User


def insert_new_user(name, email, pword):
    # create new user
    new_user = User(user_name=name, user_email=email, user_pword=pword, user_age=0, user_race='', user_gender='', user_edu='')
    # add to the db
    db.session.add(new_user)
    db.session.commit()
    db.session.close()


def check_users():
    q = db.session.query(User).all()
    for inst in q:
        print(inst.user_name)


def account_sign_in(accName, pword):
    if '@' in accName:
        email = accName
        q = db.session.query(User).filter_by(user_email=email).first()
    else:
        name = accName
        q = db.session.query(User).filter_by(user_name=name).first()
    db.session.close()
    if check_password_hash(q.user_pword, pword):
        return q
    return None


def user_query(data, opt=0):
    q = None
    if opt is 0: q = db.session.query(User).filter_by(user_id=data).first()
    elif opt is 1: q = db.session.query(User).filter_by(user_name=data).first()
    elif opt is 2: q = db.session.query(User).filter_by(user_email=data).first()
    elif opt is 3: q = db.session.query(User).filter_by(user_pword=data).first()
    db.session.close()
    return q


def user_exists(user_name):
    q = db.session.query(User).filter_by(user_name=user_name).first()
    if q is None:
        return False
    else:
        return True


def update_user_demographic_info(name, age, race, gender, edu):
    q = user_query(name,1)
    print('q.user_name from update demo', q.user_name)
    if q is not None:
        q.user_age = int(age)
        q.user_race = race
        q.user_gender = gender
        q.user_edu = edu
        print('demo updated!')
        db.session.add(q)
        db.session.commit()
        return True
    return False






