#!/usr/bin/env python3.6
import secrets
import string
from user_credentials import User, Credentials

def create_user(fname,lname,password):
        '''
        Function to create a new user account

        '''

        new_user = User(fname,lname,password)
        return new_user

def save_user(user):
        '''
        Function to save a new user account

        '''
        user.save_user()

def verify_user(first_name,password):


        '''
        Functin that checks the existence of the user before creating credential
        '''
        
        check_user = Credentials.user_login(first_name,password)
        return check_user



def generate_passwords():

        '''
        Function to generate a 7 character password for a credential
        '''
        N = 7
        gen_pass = ''.join(secrets.choice(string.ascii_lowercase + string.digits)
        for i in range(N))
        return gen_pass

def create_credential(a_account,f_name,l_name,e_email,p_password): 
        '''
        Function to create a new
        '''

        new_credential = Credentials(a_account,f_name,l_name,e_email,p_password)
        return new_credential

def save_credential(credential):
        '''
        Function to save a new credential that has been created
        '''
        Credentials.save_credentials(credential)

def display_credentials(self):
        '''
        Function to display credentials saved by a user
        '''
        return Credentials.display_credentials()        
def copy_credentials(a_account):
        '''
        Function to copy a credential's details to the clipboard
        '''
        return Credentials.copy_credentials(a_account)

def main():
        
        print("Hello, Welcome to password locker, enter user name")
        u_name = input()
        print(f"Hey, {u_name}. What would you like to do?")
        print("\n")

        while True:

                print("Enter this codes to navigate: \n ca :Create an account \n li :Login \n ex :Exit")

                short_code = input("Enter a choice: ").lower()

                if short_code == "ex":
                        break

                elif short_code == "ca":

                        print("To create a new account:")
                        f_name = input("Enter first name \n")
                        l_name = input("Enter last name \n")
                        p_word = input("Enter your password \n")

                        save_user(create_user(f_name,l_name,p_word))
                        print("\n")
                        print(f"New Account created for: \n {f_name}  {l_name} \n Your password is: {p_word}")
                        
                elif short_code == "li":


                        print("To login, enter your account details as instructed:")

                        user_name = input("Enter your first name \n")
                        password = input("Enter your password \n")

                        user_exists = verify_user(user_name,password)

                        if user_exists == user_name:
                                print(f"Welcom {user_name}. Choose an option to continue please!")
                                print("-" * 30)


                                while True:

                                        print("Navigation codes are as follows: \n cc :Create a credential \n dc :Display credentials \n co :Copy credentials \n ex :Exit")

                                        short_code = input("Enter your choice: \n ").lower()

                                        if short_code == "ex":
                                                print(f"Goodbye {user_name}")
                                                break

                                        elif short_code == "cc":
                                                print("Enter your credential details:")
                                                a_account = input("Enter the accounts name \n")
                                                f_name = input("Enter your first name \n")
                                                e_email = input("Enter your email \n")

                                                while True:
                                                        print("Choose option for entering a password:")
                                                        print("\n")

                                                        print(" ep :Enter your own passsword \n gp :Automatically generate a password \n ex :exit")

                                                        p_choice = input("Enter your option \n").lower()

                                                        if p_choice == "ep":


                                                                        print("Enter your password")
                                                                        p_password = input("Enter your password: \n")
                                                                        break

                                                        elif p_choice == "gp":
                                                                        p_password = generate_passwords()
                                                                        break

                                                        elif p_choice == "ex":
                                                                        break

                                                        else:
                                                                        print("OOOPS!!! Wrong choice entered try again")                
                                                save_credential(create_credential(a_account,f_name,l_name,e_email,p_password))

                                                print(f"Credentials have been created: \n Account name: {a_account} \n Password: {p_password}")
                                                print("\n")
                        else:
                                        print("Account does not exist create account to login")
                                        print("\n") 
                        

if __name__ == "__main__":
    main()


