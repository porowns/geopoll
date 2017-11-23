import unittest
import utils.poll as Poll

class TestUserMethods(unittest.TestCase):

    def testPollCreate(self):
        self.poll = Poll.create_poll()
        print ("Created Poll")

    def testPollUpdate(self):
        self.poll = Poll.create_poll()
        Poll.update_poll(self.poll)
        print ("Updated Poll")

    def testPollDelete(self):
        self.poll = Poll.create_poll()
        Poll.delete_poll(self.poll)
        print ("Deleted Poll")

    def testPollView(self):
        self.poll = Poll.create_poll()
        Poll.view_poll(self.poll)
        print ("Poll is viewable")


if __name__ == '__main__':
    unittest.main()