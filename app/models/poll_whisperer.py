import sqlalchemy
from sqlalchemy.orm import sessionmaker, session
from app import db, models
from app.models.table_declaration import Poll, Question
from app.models.user_whisperer import user_query


def insert_new_poll(title, user_name):
    # insert poll
    q = user_query(user_name,1)
    new_poll = Poll(poll_title=title, poll_user_id=q.user_id)
    db.session.add(new_poll)
    db.session.commit()
    db.session.close()


def insert_new_question(question_type, question_text, poll_id):
    # connect to database
    new_question = Question(
        question_type="response",
        question_text=question_text,
        question_poll_id=poll_id
        )
    # insert question
    db.session.add(new_question)
    db.session.commit()
    db.session.close()


# choice based question
def insert_new__choice(question_text, choices, poll_id):
    """ Accepts an array of strings, choices."""
    choices = ",".join(choices)
    new_question = Question(
        question_type="choice",
        question_choices=choices,
        question_text=question_text,
        question_poll_id=poll_id
        )
    # insert question
    db.session.add(new_question)
    db.session.commit()
    db.session.close()


def poll_search(data):
    q = db.session.query(Poll).filter_by(poll_title=data).all()
    return q

def get_poll(poll_id):
    q = db.session.query(Poll).filter_by(poll_id=poll_id).first()
    db.session.close()
    return q

def get_polls_by_user(user_id):
    polls = db.session.query(Poll).filter_by(poll_user_id=user_id).all()
    db.session.close()
    return polls
