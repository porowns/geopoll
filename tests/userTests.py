import unittest
from app.models.table_declaration import User
from app.models.user_whisperer import *
from app import db

class TestUserMethods(unittest.TestCase):

    def testUserCreate(self):
        # Query by name
        new_user = db.session.query(User).filter_by(user_id=1).first()
        if new_user is None:
            # create new user
            name = 'Unit Test User'
            password = 'UnitTestPassword'
            email = 'UnitTestEmail@email.com'
            insert_new_user(name, password, email)
            print ("Created User")
            self.assertTrue(new_user.user_name == name)
            self.assertTrue(new_user.user_pword == password)
        else:
            print("User had already been created. To test this again, delete the database and rerun")

    def testUserQuery(self):
        # Query by name
        new_user = db.session.query(User).filter_by(user_id=1).first()
        name = new_user.user_name
        email = new_user.user_email
        password = new_user.user_pword
        if new_user is None:
            # create new user
            name = 'Unit Test User'
            password = 'UnitTestPassword'
            email = 'UnitTestEmail@email.com'
            insert_new_user(name, password, email)

        # Query by name
        nameQuery = user_query(name, 1)
        self.assertTrue(nameQuery.user_name == name)
        self.assertTrue(nameQuery.user_email == email)
        self.assertTrue(nameQuery.user_pword == password)

        #Query by email
        emailQuery = user_query(email, 2)
        self.assertTrue(emailQuery.user_name == name)
        self.assertTrue(emailQuery.user_email == email)
        self.assertTrue(emailQuery.user_pword == password)

        # Query by password
        pwordQuery = user_query(password, 3)
        self.assertTrue(pwordQuery.user_name == name)
        self.assertTrue(pwordQuery.user_email == email)
        self.assertTrue(pwordQuery.user_pword == password)

        # Query by id
        id = nameQuery.user_id
        idQuery = user_query(id, 0)
        self.assertTrue(idQuery.user_name == name)
        self.assertTrue(idQuery.user_email == email)
        self.assertTrue(idQuery.user_pword == password)

    def testUserUpdate(self):
        print ("Updated user")
        """
        Once update_user is made we will assert that self.user's 
        properties fit the new properties given
        """

    def testUserDelete(self):
        print ("Deleted user")
        """
        Once delete_user is made we will assert that self.user
        no longer exists or is null
        """

if __name__ == '__main__':
    unittest.main()