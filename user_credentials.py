import math
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

                @classmethod
                def login_by_password(cls,number):
                                for user in cls.users_list:
                                        if user.password == number:
                                                return user          


class Credentials:

                '''
                To generate new instances of users
                '''
                credentials_lists = []

                def __init__(self,f_name,l_name,e_email,p_password):
                                self.f_name = f_name
                                self.l_name = l_name
                                self.e_email = e_email
                                self.p_password = p_password


                def save_credentials(self):
                                '''
                                save_credentials method saves users objects into credentials_lists

                                '''
                                Credentials.credentials_lists.append(self)



              
        
