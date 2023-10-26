import unittest
from models.review import Review
from datetime import datetime
import json
import os
from models import storage

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_review_creation(self):
        # Verify that a Review is created correctly
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_serialization(self):
        # Verify if the review can be serialized and deserialized
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        new_review = Review(**review_dict)
        self.assertEqual(self.review.place_id, new_review.place_id)
        self.assertEqual(self.review.user_id, new_review.user_id)
        self.assertEqual(self.review.text, new_review.text)

    def test_review_storage(self):
        storage.new(self.review)
        storage.save()
        # Check if the Review is stored correctly in FileStorage
        self.assertIn(self.review, storage.all(Review))

if __name__ == '__main__':
    unittest.main()
