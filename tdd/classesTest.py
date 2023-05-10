import unittest 
from classes import UserRegistrationService, User

class UserRegistrationTests(unittest.TestCase):
    def test_when_registering_already_existing_should_return_error(self):
        #arrange
        sut = UserRegistrationService()
        sut.Users.append( User("a.b@c.se", "Stefan") )
        #act'
        result = sut.Register("a.b@c.se", "Stefan")
        #assert
        self.assertFalse(result)

    def test_when_registering_not_existing_should_return_ok(self):
        #arrange
        sut = UserRegistrationService()
        sut.Users.clear()
        #act'
        result = sut.Register("a.b@c.se",    "Stefan")
        user = sut.FindUser("a.b@c.se")
        #assert
        self.assertTrue(result)
        self.assertIsNotNone(user)


    def test_when_registering_and_using_invalid_email_should_return_error(self):
        #arrange
        sut = UserRegistrationService()
        sut.Users.clear()
        #act'
        result = sut.Register("a.bc.se",    "Stefan")
        #assert
        self.assertFalse(result)

unittest.main()