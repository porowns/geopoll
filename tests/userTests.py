import unittest
from models.table_declaration import User, engine
from models.user_whisperer import insert_new_user, account_sign_in, user_query

class TestUserMethods(unittest.TestCase):

    def testUserCreate(self):
        name = 'name'
        password = 'password'
        email = 'email@email.com'
        insert_new_user(name, password, email)
        print ("Created user")
        """
        Once create_user is made we will assert that self.user 
        has all the desired properties here
        """

    def testUserQuery(self):
        name = 'name'
        email = 'email@email.com'
        password = 'password'
        insert_new_user(name, email, password)

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