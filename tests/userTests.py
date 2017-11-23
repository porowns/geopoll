import unittest
import utils.user as User

class TestUserMethods(unittest.TestCase):

    def testUserCreate(self):
        self.user = User.create_user()
        print ("Created user")
        """
        Once create_user is made we will assert that self.user 
        has all the desired properties here
        """

    def testUserUpdate(self):
        self.user = User.create_user()
        # Update user with new properties here
        User.update_user(self.user)
        print ("Updated user")
        """
        Once update_user is made we will assert that self.user's 
        properties fit the new properties given
        """

    def testUserDelete(self):
        self.user = User.create_user()
        User.delete_user(self.user)
        print ("Deleted user")
        """
        Once delete_user is made we will assert that self.user
        no longer exists or is null
        """

if __name__ == '__main__':
    unittest.main()