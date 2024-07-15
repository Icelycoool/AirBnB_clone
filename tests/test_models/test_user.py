#!/usr/bin/python3
"""
Unittest for the user class.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the User class"""

    def setUp(self):
        pass

    def test_email_assignment(self):
        """Test User email assignment"""
        user = User()
        user.email = "user@email.com"
        self.assertEqual(user.email, "user@email.com")

    def test_password_assignment(self):
        """Test User password assignment"""
        user = User()
        user.password = "password"
        self.assertEqual(user.password, "password")

    def test_first_name_assignment(self):
        """Test User first_name assignment"""
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_last_name_assignment(self):
        """Test User last_name assignment"""
        user = User()
        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

if __name__ == "__main__":
    unittest.main()
