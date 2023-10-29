import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import json
from models import storage
from models import FileStorage


class TestUser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_type_atrr(self):
        user = User()
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)
        self.assertEqual(type(user.email), str)

    def test_inherence(self):
        user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attributes(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        user = User()
        user.email = "test@example.com"
        user_dict = user.to_dict()
        self.assertEqual(user_dict["email"], "test@example.com")

    def test_dif_id(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_doc(self):
        self.assertIsNotNone(User.__doc__)


if __name__ == '__main__':
    unittest.main()
