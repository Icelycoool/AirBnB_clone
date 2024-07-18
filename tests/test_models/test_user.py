#!/usr/bin/python3
"""
Unittest for the user class.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Tests the User class"""

    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """Test User attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_params(self):
        """Test User parameters"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_save_method(self):
        """Test save method"""
        self.user.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_str_method(self):
        """Test __str__ method"""
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")
        self.assertEqual(user_dict["__class__"], "User")

    def test_storage_all(self):
        """Test that storage.all() contains the new user"""
        self.user.save()
        self.assertIn(self.user, storage.all().values())


if __name__ == "__main__":
    unittest.main()
