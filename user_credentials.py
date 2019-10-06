import pyperclip
import random
class User:


                '''
                To generate new instance of users 

                '''

                users_list = []

                def __init__(self,first_name,last_name,password):
                        '''
                        __init__ method that helps us define properies for

                        Args:
                             first_name: new user first name,
                             last_name: new user last name,
                             password: new user password   


                        '''

                        self.first_name = first_name
                        self.last_name = last_name
                        self.password = password

                def save_users(self):
                        '''
                        save_users method saves users objects into user_list
                        '''
                        User.users_list.append(self)     

            


class Credentials:

                '''
                To generate new instances of users
                '''
                credentials_lists = []
                user_credentials_list = []

                @classmethod
                def user_login(cls,first_name,password):
                                '''
                                Method that checks if the name and password entered match entries in the users_list

                                '''
                                current_user = ''
                                for user in User.users_list:
                                        if (user.first_name == first_name and user.password == password):
                                                        current_user = user.first_name
                                                        return current_user


                def __init__(self,a_account,f_name,l_name,e_email,p_password):

                                self.a_account = a_account
                                self.f_name = f_name
                                self.l_name = l_name
                                self.e_email = e_email
                                self.p_password = p_password


                def save_credentials(self):
                                '''
                                save_credentials method saves users objects into credentials_lists

                                '''
                                Credentials.credentials_lists.append(self)
                @classmethod        
                def display_credentials(cls):
                                return cls.credentials_lists        
                @classmethod
                def find_by_account_name(cls,a_account):
                                '''
                                Method that takes in an account name and reurns a credential that matches that account.
                                '''

                                for credential in cls.credentials_lists:
                                                if credential.a_account == a_account:
                                                        
                                                                return credential
                @classmethod
                def copy_credentials(cls,a_account):
                                credential_found = Credentials.find_by_account_name(a_account)
                                pyperclip.copy(credential_found.a_account)