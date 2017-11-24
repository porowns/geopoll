import unittest
from models.poll_whisperer import insert_new_question, insert_new_poll
from models.table_declaration import User, Poll

class TestUserMethods(unittest.TestCase):

    def testPollCreate(self):
        title = "poll title"
        user = User(user_name = 'name', user_email = 'email@email.com', user_pword = 'password')
        insert_new_poll(title, user)
        print ("Created Poll")
        """
        Once create_poll is made we will assert that self.poll
        has all the desired properties here
        """

    def testPollUpdate(self):
        print ("Updated Poll")
        """
        Once update_poll is made we will assert that self.poll's 
        properties fit the new properties given
        """

    def testPollDelete(self):
        print ("Deleted Poll")
        """
        Once delete_poll is made we will assert that self.poll
        no longer exists or is equivalent to null
        """

    def testPollView(self):
        print ("Poll is viewable")
        """
        Once view_poll is made we will assert that self.poll is
        viewable. That or this will just have to be a test done
        manually because I cant see a way to automate this *yet*
        """


if __name__ == '__main__':
    unittest.main()