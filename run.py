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
        user.save_user(user)

def verify_user(first_name,password):


        '''
        Functin that checks the existence of the user before creating credential
        '''
        
        check_user = Credentials.user_login(first_name,password)
        return check_user



def generate_passwords():

        '''
        Function to generate an 7 character password for a crede
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

