#!/usr/bin/python3
"""
Unittest for the user class.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the User class"""

    def setUp(self):
        self.user = User()

    def test_email_assignment(self):
        """Test User email assignment"""
        self.user.email = "user@email.com"
        self.assertEqual(self.user.email, "user@email.com")

    def test_password_assignment(self):
        """Test User password assignment"""
        self.user.password = "password"
        self.assertEqual(self.user.password, "password")

    def test_first_name_assignment(self):
        """Test User first_name assignment"""
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_last_name_assignment(self):
        """Test User last_name assignment"""
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")

if __name__ == "__main__":
    unittest.main()
