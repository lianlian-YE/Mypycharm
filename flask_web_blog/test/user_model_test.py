import unittest
from models import User
class userModelTestCase(unittest.TestCase):
    def test_setter_passwd(self):
        u=User(password='test')
        self.assertTrue(u.password_hash is not None)
    def test_no_passwd_getter(self):
        u = User(password='test')
        with self.assertRaises(AttributeError):
            u.password
    def test_passwd_verification(self):
        u = User(password='test')
        self.assertTrue(u.verify_password('test'))
        self.assertFalse(u.verify_password('debug'))
    def test_passwd_salts_are_random(self):
        u = User(password='test')
        u2= User(password='test2')
        self.assertTrue(u.password_hash!=u2.password_hash)

if __name__=='__main__':
    unittest.main()