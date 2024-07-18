#!/usr/bin/python3
"""
Unittest for the Place class.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Tests the Place class"""

    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """Test Place attributes"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_params(self):
        """Test Place parameters"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_save_method(self):
        """Test save method"""
        self.place.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_str_method(self):
        """Test __str__ method"""
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        self.place.city_id = "001"
        self.place.user_id = "0001"
        self.place.name = "Towfiiq"
        self.place.description = "Two Story"
        self.place.number_rooms = 5
        self.place.number_bathrooms = 3
        self.place.max_guest = 7
        self.place.price_by_night = 630
        self.place.latitude = 1.05
        self.place.longitude = 1.01
        self.place.amenity_ids = ['001', '002']

        place_dict = self.place.to_dict()

        self.assertIsInstance(place_dict["id"], str)
        self.assertEqual(place_dict["city_id"], "001")
        self.assertEqual(place_dict["user_id"], "0001")
        self.assertEqual(place_dict["name"], "Towfiiq")
        self.assertEqual(place_dict["description"], "Two Story")
        self.assertEqual(place_dict["number_rooms"], 5)
        self.assertEqual(place_dict["number_bathrooms"], 3)
        self.assertEqual(place_dict["max_guest"], 7)
        self.assertEqual(place_dict["price_by_night"], 630)
        self.assertEqual(place_dict["latitude"], 1.05)
        self.assertEqual(place_dict["longitude"], 1.01)
        self.assertEqual(place_dict["amenity_ids"], ['001', '002'])
        self.assertEqual(place_dict["__class__"], "Place")

    def test_storage_all(self):
        """Test that storage.all() contains the new user"""
        self.place.save()
        self.assertIn(self.place, storage.all().values())


if __name__ == "__main__":
    unittest.main()
