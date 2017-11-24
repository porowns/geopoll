import sqlalchemy
from sqlalchemy.orm import sessionmaker, session
from table_declaration import Poll, PollResponse, Question, Answer, engine, inspect, Table

def insert_new_poll(title, user):
    Session = sessionmaker(bind=engine)
    session = Session()
    # insert poll
    new_poll = Poll(poll_title=title, poll_user_id=user)
    session.add(
            new_poll
            )
    session.commit()
    session.close()

def insert_new_question(question_type, question_text, poll_id):
    # connect to database
    Session = sessionmaker(bind=engine)
    session = Session()
    new_question = Question(
        question_type=question_type,
        question_text=question_text,
        question_poll_id=poll_id
        )
    # insert question
    session.add(
            new_question
        )
    session.commit()
    session.close()
