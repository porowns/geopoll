import unittest
import sys
from app.models.poll_whisperer import *
from app.models.user_whisperer import user_query
from app.models.table_declaration import User, Poll, Question, PollResponse
from app import db
from random import randint

new_user = None

class TestPollMethods(unittest.TestCase):

    def setUp(self):
        """
            since no delete methods are available a universal user will be checked for each test
            if said user is not there, it will be created
        """
        # Query by name
        new_user = db.session.query(User).filter_by(user_id=1).first()
        if new_user is None:
            # create new user
            new_user = User(user_name="Unit Test User", user_email="UnitTestEmail@email.com",
                            user_pword="UnitTestPassword", user_age=0, user_race='',
                            user_gender='', user_edu='', user_id="1")
            # add to the db
            db.session.add(new_user)
            db.session.commit()
            db.session.close()

    def testPollCreate(self):
        """
            since no delete methods are available a universal poll will be checked for each test
            if said poll is not there it will be created
            This test is different because it is testing creation of a poll
        """
        new_poll = db.session.query(Poll).filter_by(poll_id=1).first()
        if new_poll is None:
            title = "Unit Test Poll"
            insert_new_poll(title, new_user.user_name)
            print ("Created Poll")
            """
            Once create_poll is made we will assert that self.poll
            has all the desired properties here
            """
            dbPoll = db.session.query(Poll).filter_by(poll_title=title).first()
            self.assertTrue(dbPoll.poll_title == title)
        else:
            print("Poll was already created. Delete the db (or the poll if you can do it safely) to re-run the test")

    def testPollQuestionCreate(self):
        """
            since no delete methods are available a universal poll will be chekced for each test
            if said poll is not there it will be created
        """
        new_poll = db.session.query(Poll).filter_by(poll_id=1).first()
        if new_poll is None:
            # create new poll
            new_poll = Poll(poll_title='Unit Test Poll', poll_user_id=new_user.user_id, poll_id=1, poll_published=0)
            # add to the db
            db.session.add(new_poll)
            db.session.commit()
            db.session.close()

        rand = randint(0, sys.maxsize)
        questionText = 'Unit Test Question #'
        questionText += str(rand)
        pollID = new_poll.poll_id
        insert_new_question(question_text=questionText, choices=None, poll_id=pollID)
        print("New Response Question Created")
        dbQuestions = db.session.query(Question).filter_by(question_poll_id=pollID).all()
        dbq = None
        for q in dbQuestions:
            if q.question_text == questionText:
                dbq = q
        self.assertTrue(dbq is not None)
        self.assertTrue(dbq.question_text == questionText)
        self.assertTrue(dbq.question_type == "response")
        self.assertTrue(dbq.question_choices == None)
        self.assertTrue(dbq.question_poll_id == pollID)

    def testPollChoiceQuestionCreate(self):
        """
            since no delete methods are available a universal poll will be chekced for each test
            if said poll is not there it will be created
        """
        new_poll = db.session.query(Poll).filter_by(poll_id=1).first()
        if new_poll is None:
            # create new poll
            new_poll = Poll(poll_title='Unit Test Poll', poll_user_id=new_user.user_id, poll_id=1, poll_published=0)
            # add to the db
            db.session.add(new_poll)
            db.session.commit()
            db.session.close()

        rand = randint(0, sys.maxsize)
        questionText = 'Unit Test Question #'
        questionText += str(rand)
        pollID = new_poll.poll_id
        choices = 'Kaleb, Nick, Keaton'
        insert_new_question(question_text=questionText, choices=choices, poll_id=pollID)
        print("New Choice Question Created")
        dbQuestions = db.session.query(Question).filter_by(question_poll_id=pollID).all()
        dbq = None
        for q in dbQuestions:
            if q.question_text == questionText:
                dbq = q
        self.assertTrue(dbq is not None)
        self.assertTrue(dbq.question_text == questionText)
        self.assertTrue(dbq.question_type == "choice")
        self.assertTrue(dbq.question_choices == choices)
        self.assertTrue(dbq.question_poll_id == pollID)

    def testPollResponse(self):
        """
            since no delete methods are available a universal poll will be chekced for each test
            if said poll is not there it will be created
        """
        new_poll = db.session.query(Poll).filter_by(poll_id=1).first()
        if new_poll is None:
            # create new poll
            new_poll = Poll(poll_title='Unit Test Poll', poll_user_id=new_user.user_id, poll_id=1, poll_published=0)
            # add to the db
            db.session.add(new_poll)
            db.session.commit()
            db.session.close()

        """
            this question involves the use of at least one question in the poll. Query the poll
             and if it has no questions, create one
        """
        poll_q = db.session.query(Question).filter_by(question_type="response").first()
        if poll_q is None:
            # create new question
            rand = randint(0, sys.maxsize)
            questionText = 'Unit Test Question #'
            questionText += str(rand)
            poll_q = Question(question_poll_id=new_poll.poll_id, question_text=questionText, question_type="response",
                              question_choices=None)
            db.session.add(poll_q)
            db.session.commit()
            db.session.close()

        # do a poll response
        questions = str(poll_q)
        answers = "This is an answer to a Unit Test Question"
        insert_new_response(new_poll.poll_id, questions=questions, answers=answers)
        print("Responded to a Question")
        """
        if(publish_poll(new_poll.poll_id)):
            dbResponses = db.session.query(PollResponse).filter_by(poll_id=new_poll.poll_id).all()
            dbr = None
            for r in dbResponses:
                if r.poll_response_answers == answers:
                    dbr = r
            self.assertTrue(dbr is not None)
            self.assertTrue(dbr.poll_response_answers == answers)
            self.assertTrue(dbr.poll_response_questions == questions)
            self.assertTrue(dbr.poll_id == new_poll.poll_id)
        else:
            print("Poll not published")
            self.fail("Publish_poll did not succeed")
        """

    def testPollChangeTitle(self):
        """
            since no delete methods are available a universal poll will be chekced for each test
            if said poll is not there it will be created
        """
        new_poll = db.session.query(Poll).filter_by(poll_id=1).first()
        if new_poll is None:
            # create new poll
            new_poll = Poll(poll_title='Unit Test Poll', poll_user_id=new_user.user_id, poll_id=1, poll_published=0)
            # add to the db
            db.session.add(new_poll)
            db.session.commit()
            db.session.close()

        new_title = "New Unit Test Poll"
        if change_poll_title(new_poll.poll_id, new_title):
            print("Successfully Changed Poll's Name")
            dbPoll = db.session.query(Poll).filter_by(poll_id=1).first()
            self.assertTrue(dbPoll.poll_title == new_title)
            self.assertTrue(change_poll_title(new_poll.poll_id, 'Unit Test Poll'))
            self.assertTrue(dbPoll.poll_title == 'Unit Test Poll')
        else:
            print("Did not change poll's name")
            self.fail(msg='Change_poll_title did not work')

    def testPublishPoll(self):
        """
            since no delete methods are available a universal poll will be chekced for each test
            if said poll is not there it will be created
        """
        new_poll = db.session.query(Poll).filter_by(poll_id=1).first()
        if new_poll is None:
            # create new poll
            new_poll = Poll(poll_title='Unit Test Poll', poll_user_id=new_user.user_id, poll_id=1, poll_published=0)
            # add to the db
            db.session.add(new_poll)
            db.session.commit()
            db.session.close()

        if(publish_poll(new_poll.poll_id)):
            print("Successfully Published the Poll")
            self.assertTrue(new_poll.poll_published == 1)
            new_poll.poll_published = 0
            self.assertTrue(new_poll.poll_published == 0)


    def testPollUpdate(self):
        print ("Updated Poll")
        """
        Once update_poll is made we will assert that self.poll's 
        properties fit the new properties given
        """

    def testPollQuestionUpdate(self):
        """
        A test to test updating a question already created
        """
        pass

    def testPollDelete(self):
        print ("Deleted Poll")
        """
        Once delete_poll is made we will assert that self.poll
        no longer exists or is equivalent to null
        """

    def testPollQuestionDelete(self):
        """
        A test to test deleting a question already created
        """
        pass

    def testPollView(self):
        print ("Poll is viewable")
        """
        Once view_poll is made we will assert that self.poll is
        viewable. That or this will just have to be a test done
        manually because I cant see a way to automate this *yet*
        """

    def testPollAddQuestion(self):
        """
        A test to test adding a question to a poll
        """
        pass


if __name__ == '__main__':
    unittest.main()