import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import json
from models import storage


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        pass

    def test_review_creation(self):
        # Verify that a Review is created correctly
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_serialization(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        new_review = Review(**review_dict)
        self.assertEqual(self.review.place_id, new_review.place_id)
        self.assertEqual(self.review.user_id, new_review.user_id)
        self.assertEqual(self.review.text, new_review.text)

    def test_type_attr(self):
        rev = Review()
        rev.place_id = "p4"
        rev.user_id = "234"
        rev.text = "i like it"

        self.assertEqual(type(rev.place_id), str)
        self.assertEqual(type(rev.user_id), str)
        self.assertEqual(type(rev.text), str)

    def test_diff_id(self):
        rev = Review()
        other = Review()
        self.assertNotEqual(rev.id, other.id)

    def test_doc(self):
        self.assertIsNotNone(Review.__doc__)


if __name__ == '__main__':
    unittest.main()
