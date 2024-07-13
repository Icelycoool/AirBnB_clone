#!/usr/bin/python3
"""Test Module for File Storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest, TestCase):
    """
    Unittetst for FileStorage class
    """

    def setUp(self):
        """
        Set up test methods
        """
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up after test methods"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new method"""
        mode = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.save()

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test the reload method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
