from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Sequence
from sqlalchemy_utils import ChoiceType

Base = declarative_base()

# association table for Poll->Question relationships
poll_question_relationship = db.Table('poll_question_relationship',
        Base.metadata,
        db.Column('poll_id', db.Integer, ForeignKey('polls.poll_id')),
        db.Column('question_id', db.Integer, ForeignKey('questions.question_id'))
        )

# types of questions
QUESTION_TYPES = [
        (u'choice', u'choice'),
        (u'response', u'response')
]


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,Sequence('user_id_seq'), primary_key=True)
    user_name = db.Column(db.String(20), unique=True)
    user_email = db.Column(db.String(20), unique=True)
    user_pword = db.Column(db.String(15))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)


class Question(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True)
    question_type = ChoiceType(QUESTION_TYPES)
    question_text = db.Column(db.String(50))
    question_poll_id = db.Column(db.Integer, ForeignKey('polls.poll_id'))


class Answer(db.Model):
    __tablename__ = "answers"
    answer_id = db.Column(db.Integer, primary_key=True)
    poll_answer = db.Column(db.String(50))


class Poll(db.Model):
    __tablename__= 'polls'
    poll_id = db.Column(db.Integer, primary_key=True)
    poll_title = db.Column(db.String(50))
    poll_user_id = db.Column(db.Integer, ForeignKey('users.user_id'))
    poll_questions = db.relationship('Question', backref='q', lazy='dynamic')
    poll_responses = db.relationship('PollResponse', backref='r', lazy='dynamic')


class PollResponse(db.Model):
    __tablename__ = 'poll_responses'
    poll_response_id = db.Column(db.Integer, primary_key=True)
    poll_response_user = db.Column(db.Integer, ForeignKey('users.user_id'))
    poll_id = db.Column(db.Integer, ForeignKey('polls.poll_id'))