#!/usr/bin/python3
"""Unittest for the Amenity class"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """Test the Amenity class attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_params(self):
        """Test Amenity class parameters"""
        self.assertIsInstance(self.amenity.name, str)

    def test_save_method(self):
        """Test save method"""
        self.amenity.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_str_method(self):
        """test __str__ method"""
        expected_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        self.amenity.name = "Pool"
        city_dict = self.amenity.to_dict()
        self.assertEqual(city_dict["name"], "Pool")

    def test_storage_all(self):
        """Test that storag.all() contains the new state"""
        self.amenity.save()
        self.assertIn(self.amenity, storage.all().values())


if __name__ == "__main__":
    unittests.main()
