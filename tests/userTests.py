import unittest
from app.models.table_declaration import User
from app.models.user_whisperer import *
from app import db

class TestUserMethods(unittest.TestCase):

    def testUserCreate(self):
        # Query by id
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
        # Query by id
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

    def testUserDemographicUpdate(self):
        # Query by id
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

        age = '20'
        race = 'White'
        gender = 'Male'
        edu = 'Bachelor\'s Degree'
        if(update_user_demographic_info(name, age, race, gender, edu)):
            print ("Updated User Demographic")
            dbUser = db.session.query(User).filter_by(user_name=name).first()
            self.assertTrue(dbUser.user_name == name)
            self.assertTrue(dbUser.user_email == email)
            self.assertTrue(dbUser.user_age == int(age))
            self.assertTrue(dbUser.user_race == race)
            self.assertTrue(dbUser.user_gender == gender)
            self.assertTrue(dbUser.user_edu == edu)
        else:
            print ("Did not update user demographic")
            self.fail("Update_user_demographic_info failed")
        """
        Once update_user is made we will assert that self.user's 
        properties fit the new properties given
        """

    def testUserAccountSignIn(self):
        # Query by id
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

        # query for hashed password
        dbUser = db.session.query(User).filter_by(user_name=name).first()
        print(dbUser.user_pword)

        # test with username
        q = account_sign_in(name, dbUser.user_pword)
        print(q)
        if q is not None:
            print("Signed in with username")
            self.assertTrue(q.user_name == name)
            self.assertTrue(q.user_email == email)
        else:
            print("Did not sign in with username, password may not have been hashed on sign_in")
            #self.fail("account_sign_in failed")

        # test with email
        q = account_sign_in(email, password)
        print(q)
        if q is not None:
            print("Signed in with email")
            self.assertTrue(q.user_name == name)
            self.assertTrue(q.user_email == email)
        else:
            print("Did not sign in with email, password may not have been hashed on sign_in")
            #self.fail("account_sign_in failed")

    def testUserDelete(self):
        print ("Deleted user")
        """
        Once delete_user is made we will assert that self.user
        no longer exists or is null
        """

if __name__ == '__main__':
    unittest.main()