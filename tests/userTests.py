import unittest
import utils.user as User

class TestUserMethods(unittest.TestCase):

    def testUserCreate(self):
        self.user = User.create_user()
        print ("Created user")

    def testUserUpdate(self):
        self.user = User.create_user()
        User.update_user(self.user)
        print ("Updated user")

    def testUserDelete(self):
        self.user = User.create_user()
        User.delete_user(self.user)
        print ("Deleted user")


if __name__ == '__main__':
    unittest.main()