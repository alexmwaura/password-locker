import unittest
import pyperclip
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
                self.new_user.save_user()
                self.assertEqual(len(User.users_list),1)

        
                         

class TestCredentials(unittest.TestCase):
                '''

                Test class that defines test case for Credentials class behaviour 

                '''
                def test_user_login(self):

                        '''
                        Function to test whether the login in function login_user works as expected
                        '''
                        self.new_user = User("Alex","mwaura","12345")
                        self.new_user.save_user()
                        user_login = User("test","user","1122")
                        user_login.save_user()

                        for user in User.users_list:
                                        if user.first_name == user_login.first_name and user.password == user_login.password:
                                                        current_user = user.first_name
                                                        return current_user
                                                        
                        

                def setUp(self):
                                self.new_credential = Credentials("instagram","Alex","mwaura","alexmwaura@gmail.com","12345")

                def tearDown(self):


                                Credentials.credentials_lists = []

                def test_init(self):

                                self.assertEqual(self.new_credential.a_account,"instagram") 
                                self.assertEqual(self.new_credential.f_name,"Alex")
                                self.assertEqual(self.new_credential.l_name,"mwaura")
                                self.assertEqual(self.new_credential.e_email,"alexmwaura@gmail.com")
                                self.assertEqual(self.new_credential.p_password,"12345")

                def save_credentials(self):
                        
                                self.new_credential.save_credentials()
                                self.assertEqual(len(Credentials.credentials_lists),1)




                def test_save_multiple_credentials(self):
                                self.new_credential.save_credentials()
                                test_credentials = Credentials("account","test","user","test@user","12345")
                                test_credentials.save_credentials()
                                self.assertEqual(len(Credentials.credentials_lists),2)


                def test_display_credentials(self):   
                                self.assertEqual(Credentials.display_credentials(),Credentials.credentials_lists)


                def test_find_by_account_name(self):
                                '''
                                Test to check if the find_by_account_name method returns the correct credential

                                '''

                                self.new_credential.save_credentials()
                                account = Credentials("insta","test","user","test@user","12345")
                                account.save_credentials()
                                credential_exists = Credentials.find_by_account_name("insta")
                                self.assertEqual(credential_exists,account)


                def test_copy_credentials(self):
                                '''
                                Test to confirm that we are copying the email address from a found credential
                                '''

                                self.new_credential.save_credentials()
                                Credentials.copy_credentials("instagram") 

                                self.assertEqual(self.new_credential.a_account,pyperclip.paste())


                def test_delete_credentials(self):
                                '''
                                test_delete_credentials to test if we can delete credentials from our credential list
                                '''

                                self.new_credential.save_credentials()
                                test_credentials = Credentials("account","test","user","test@user","12345")
                                test_credentials.save_credentials()

                                self.new_credential.delete_credentials()
                                self.assertEqual(len(Credentials.credentials_lists),1)




if __name__ == "__main__":
        unittest.main()
    
