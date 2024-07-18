#!/usr/bin/python3
"""Unittest for the Review class"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.review import Review
from models import storage


class TestState(unittest.TestCase):
    """Tests the Review class"""

    def setUp(self):
        self.review = Review()

    def tearDown(self):
        del self.review
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """Test the Review class attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_params(self):
        """Test Review class parameters"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_save_method(self):
        """Test save method"""
        self.review.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_str_method(self):
        """test __str__ method"""
        expected_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        """Test to_dict method"""
        self.review.place_id = "0001"
        self.review.user_id = "001"
        self.review.text = "Amazing place"

        review_dict = self.review.to_dict()

        self.assertEqual(review_dict["place_id"], "0001")
        self.assertEqual(review_dict["user_id"], "001")
        self.assertEqual(review_dict["text"], "Amazing place")

    def test_storage_all(self):
        """Test that storag.all() contains the new state"""
        self.review.save()
        self.assertIn(self.review, storage.all().values())


if __name__ == "__main__":
    unittests.main()
