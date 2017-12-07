import sqlalchemy
from sqlalchemy.orm import sessionmaker, session
from app import db, models
from app.models.table_declaration import Poll, Question, PollResponse
from app.models.user_whisperer import user_query


def insert_new_poll(title, user_name):
    # insert poll
    q = user_query(user_name,1)
    new_poll = Poll(poll_title=title, poll_user_id=q.user_id, poll_published=0)
    db.session.add(new_poll)
    db.session.commit()
    db.session.close()

'''
def insert_new_question(question_type, question_text, poll_id):
    # connect to database
    # insert question
    db.session.add(new_question)
    db.session.commit()
    db.session.close()

'''

# choice based question
def insert_new_question(question_text, choices, poll_id):
    if choices:
        new_question = Question(
            question_type="choice",
            question_choices=choices,
            question_text=question_text,
            question_poll_id=poll_id
            )
    else:
        new_question = Question(
            question_type="response",
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


def poll_search_name(data):
    q = db.session.query(Poll).filter_by(poll_title=data).first()
    return q


def get_poll(poll_id):
    q = db.session.query(Poll).filter_by(poll_id=poll_id).first()
    db.session.expunge(q)
    db.session.close()
    return q

def get_polls_by_user(user_id):
    polls = db.session.query(Poll).filter_by(poll_user_id=user_id).all()
    for poll in polls:
        db.session.expunge(poll)
    db.session.close()
    return polls

def get_poll_questions(poll_id):
    questions = db.session.query(Question).filter_by(question_poll_id=poll_id).all()
    for question in questions:
        db.session.expunge(question)
    return questions

def insert_new_response(poll_id, questions, answers, lat, lon):
    poll_response = PollResponse(
            poll_response_questions=questions,
            poll_response_answers=answers,
            poll_id=poll_id,
            poll_response_lat=lat,
            poll_response_lon=lon
            )
    db.session.add(poll_response)
    db.session.commit()
    db.session.close()

def get_responses(poll_id):
    responses = db.session.query(PollResponse).filter_by(poll_id=poll_id).all()
    for response in responses:
        db.session.expunge(response)
    return responses

def change_poll_title(poll_id, title):
    poll = get_poll(poll_id)
    poll.poll_title = title
    db.session.add(poll)
    db.session.commit()
    return True

def publish_poll(poll_id):
	poll = get_poll(poll_id)
	poll.poll_published = 1
	db.session.add(poll)
	db.session.commit()
	return True

def get_responses_geolocation_list(poll_id):
    responses = get_responses(poll_id)
    geolocation_list = []
    for response in responses:
        cords = []
        cords.append(response.response_lat)
        cords.append(response.response_lon)
        geolocation_list.append(cords)
    return geolocation_list

