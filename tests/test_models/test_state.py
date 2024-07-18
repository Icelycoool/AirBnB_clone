#!/usr/bin/python3
"""Unittest for the State class"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """Tests the State class"""

    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """Test the State class attributes"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_params(self):
        """Test State class parameters"""
        self.assertIsInstance(self.state.name, str)

    def test_save_method(self):
        """Test save method"""
        self.state.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_str_method(self):
        """test __str__ method"""
        expected_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        self.state.name = "Rehema state"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["name"], "Rehema state")

    def test_storage_all(self):
        """Test that storag.all() contains the new state"""
        self.state.save()
        self.assertIn(self.state, storage.all().values())


if __name__ == "__main__":
    unittests.main()
