from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Sequence
from sqlalchemy_utils import ChoiceType

engine = create_engine('sqlite:///geo_user.db', echo=False)
Base = declarative_base()

# association table for Poll->Question relationships
poll_question_relationship = Table('poll_question_relationship',
        Base.metadata,
        Column('poll_id', Integer, ForeignKey('polls.poll_id')),
        Column('question_id', Integer, ForeignKey('questions.question_id'))
        )

# types of questions
QUESTION_TYPES = [
        (u'choice', u'choice'),
        (u'response', u'response')
]

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    user_name = Column(String(50))
    user_email = Column(String)
    user_pword = Column(String(12))

class Question(Base):
    """
        Questions have an ID, type (choice or response), and text.
        Instead of making a new Choice() object, there is a choices
        string that uses comma delimited answers. (e.g one,two,three)
    """
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True)
    question_type = ChoiceType(QUESTION_TYPES)
    question_choices = Column(String(256))
    question_text = Column(String(50))
    question_poll_id = Column(Integer, ForeignKey('polls.poll_id'))

class Answer(Base):
    """
        Answers are attached to a single question.
        Each answer has answer text, which can be a fill-in blank answer,
        or a modal selection from a question with choices.

    """
    __tablename__ = "answers"
    answer_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.question_id'))
    answer_text = Column(String(50))

class Poll(Base):
    __tablename__= 'polls'
    poll_id = Column(Integer, primary_key=True)
    poll_title = Column(String(50))
    poll_user_id = Column(Integer, ForeignKey('users.user_id'))
    poll_questions = relationship("Question", secondary=poll_question_relationship)
    poll_responses = relationship("PollResponse")

class PollResponse(Base):
    __tablename__ = 'poll_responses'
    poll_response_id = Column(Integer, primary_key=True)
    poll_response_user = Column(Integer, ForeignKey('users.user_id'))
    poll_id = Column(Integer, ForeignKey('polls.poll_id'))

Base.metadata.create_all(engine)
