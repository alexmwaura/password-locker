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
                    


