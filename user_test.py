import unittest
from user import User

class TestUser(unittest.TestCase):
        '''
        Test class that defines test cases for user class behaviour
        '''
        def setUp(self):

                self.new_user = User("Alex","mwaura","1234")

        def test_init(self):

                self.assertEqual(self.new_user.first_name,"Alex")
                self.assertEqual(self.new_user.last_name,"mwaura")
                self.assertEqual(self.new_user.password,"1234")
                
if __name__ == "__main__":
        unittest.main()
    
