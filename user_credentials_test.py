import unittest
import random
from user_credentials import User,Credentials 

class TestUser(unittest.TestCase):
        '''
        Test class that defines test cases for user class behaviour
        '''
        def setUp(self):

                self.new_user = User("Alex","mwaura","1234")

        def tearDown(self):
                '''
                tearDown method for cleaning up after each test case has run
                '''

                User.users_list = []        

        def test_init(self):

                self.assertEqual(self.new_user.first_name,"Alex")
                self.assertEqual(self.new_user.last_name,"mwaura")
                self.assertEqual(self.new_user.password,"1234")

        def test_save_users(self):
                self.new_user.save_users()
                self.assertEqual(len(User.users_list),1)

        def test_save_multiple_users(self):

                '''
                test_save_multiple_users to check if we can save multiple users
                objects to our user_list
                '''

                self.new_user.save_users()
                test_user = User("Test","user","1122")
                test_user.save_users()
                self.assertEqual(len(User.users_list),2)

        def test_user_login(self):
                        self.new_user.save_users()
                        test_login = User("Test","user","1122")
                        test_login.save_users()

                        user_login = User.login_by_password("1122")
                        self.assertEqual(user_login.first_name,test_login.first_name)                  

class TestCredentials(unittest.TestCase):
                '''

                Test class that defines test case for Credentials class behaviour 

                '''
                def setUp(self):
                                self.new_credential = Credentials("Alex","mwaura","alexmwaura@gmail.com","12345")

                def tearDown(self):


                                Credentials.credentials_lists = []

                def test_init(self):


                                self.assertEqual(self.new_credential.f_name,"Alex")
                                self.assertEqual(self.new_credential.l_name,"mwaura")
                                self.assertEqual(self.new_credential.e_email,"alexmwaura@gmail.com")
                                self.assertEqual(self.new_credential.p_password,"12345")

                def save_credentials(self):
                        
                                self.new_credential.save_credentials()
                                self.assertEqual(len(Credentials.credentials_lists),1)




                def test_save_multiple_credentials(self):
                                self.new_credential.save_credentials()
                                test_credentials = Credentials("test","user","test@user","12345")
                                test_credentials.save_credentials()
                                self.assertEqual(len(Credentials.credentials_lists),2)


                def test_display_credentials(self):   
                                self.assertEqual(Credentials.display_credentials(),Credentials.credentials_lists)






if __name__ == "__main__":
        unittest.main()
    
