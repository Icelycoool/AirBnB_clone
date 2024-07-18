#!/usr/bin/python3
"""Unittest for the City class"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """Test the City class attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_params(self):
        """Test City class parameters"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_save_method(self):
        """Test save method"""
        self.city.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_str_method(self):
        """test __str__ method"""
        expected_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        self.city.state_id = "001"
        self.city.name = "Nairobi"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["state_id"], "001")
        self.assertEqual(city_dict["name"], "Nairobi")

    def test_storage_all(self):
        """Test that storag.all() contains the new state"""
        self.city.save()
        self.assertIn(self.city, storage.all().values())


if __name__ == "__main__":
    unittests.main()
