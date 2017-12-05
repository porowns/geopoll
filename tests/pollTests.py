import unittest
from app.models.poll_whisperer import insert_new_question, insert_new_poll
from app.models.user_whisperer import user_query
from app.models.table_declaration import User, Poll
from app import db

class TestPollMethods(unittest.TestCase):

    def testPollCreate(self):
        """
            since no delete methods are available a universal user will be checked for each test
            if said user is not there, it will be created
        """
        # Query by name
        new_user = db.session.query(User).filter_by(user_id=1).first()
        if new_user is None:
            # create new user
            new_user = User(user_name="Unit Test User", user_email="UnitTestEmail@email.com", user_pword="UnitTestPassword", user_age=0, user_race='',
                            user_gender='', user_edu='', user_id="1")
            # add to the db
            db.session.add(new_user)
            db.session.commit()
            db.session.close()

        title = "poll title"
        insert_new_poll(title, new_user.user_name)
        print ("Created Poll")
        """
        Once create_poll is made we will assert that self.poll
        has all the desired properties here
        """
        dbPoll = db.session.query(Poll).filter_by(poll_title=title).first()
        self.assertTrue(dbPoll.poll_title == title)

    def testPollQuestionCreate(self):
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
        poll = Poll(poll_title='Test', poll_user_id=new_user.user_id)
        questionType = 'Multiple Choice'
        quesitonText = 'Is this a question?'
        pollID = poll.poll_id
        insert_new_question(question_text=quesitonText, choices=None, poll_id=pollID)
        print("New Question Created")

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

    def testPollResponse(self):
        """
        A test to test poll responses however we choose to do that
        """
        pass


if __name__ == '__main__':
    unittest.main()