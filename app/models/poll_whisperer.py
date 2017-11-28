import sqlalchemy
from sqlalchemy.orm import sessionmaker, session
from app import db
from app.models.table_declaration import Poll, Question


def insert_new_poll(title, user):
    # insert poll
    new_poll = Poll(poll_title=title, poll_user_id=user)
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
