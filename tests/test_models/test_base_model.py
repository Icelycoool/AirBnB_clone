#!/usr/bin/python3
"""
Contanins BaseModel unittests
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Test class attribute of BaseModel
    """

    def setUp(self):
        """Sets up an instance of the class used in all tests"""
        self.instance = BaseModel()

    def test_id_is_string(self):
        """Tests that id is string"""
        self.assertIsInstance(self.instance.id, str)

    def test_is_datetime(self):
        """Tests that updated_at & created_at are datetime"""
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_save(self):
        """Tests that save updates the attribute `update_at`"""
        model = BaseModel()
        initial_updated = self.instance.updated_at
        self.instance.save()
        last_updated = self.instance.updated_at
        self.assertNotEqual(initial_updated, last_updated)
        self.assertTrue(last_updated > initial_updated)

    def test_to_dict(self):
        """Tests the to_dict method"""
        instance_dict = self.instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('__class__', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')

    def test_str_method(self):
        """Test the __str__ method"""
        instance_str = str(self.instance)
        self.assertIn('[BaseModel]', instance_str)
        self.assertIn('id', instance_str)
        self.assertIn('created_at', instance_str)
        self.assertIn('updated_at', instance_str)

if __name__ == '__main__':
    unittest.main()
