import unittest
import utils.poll as Poll

class TestUserMethods(unittest.TestCase):

    def testPollCreate(self):
        self.poll = Poll.create_poll()
        print ("Created Poll")
        """
        Once create_poll is made we will assert that self.poll
        has all the desired properties here
        """

    def testPollUpdate(self):
        self.poll = Poll.create_poll()
        # Update poll with new properties here
        Poll.update_poll(self.poll)
        print ("Updated Poll")
        """
        Once update_poll is made we will assert that self.poll's 
        properties fit the new properties given
        """

    def testPollDelete(self):
        self.poll = Poll.create_poll()
        Poll.delete_poll(self.poll)
        print ("Deleted Poll")
        """
        Once delete_poll is made we will assert that self.poll
        no longer exists or is equivalent to null
        """

    def testPollView(self):
        self.poll = Poll.create_poll()
        Poll.view_poll(self.poll)
        print ("Poll is viewable")
        """
        Once view_poll is made we will assert that self.poll is
        viewable. That or this will just have to be a test done
        manually because I cant see a way to automate this *yet*
        """


if __name__ == '__main__':
    unittest.main()