##!/usr/bin/python3

"""
Unit tests for the FileStorage class
"""

import unittest
import os
from models import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        self.storage = FileStorage()
        self.user = User()

    def tearDown(self):
        pass

    def test_all(self):
        """
        Test the 'all' method
        """
        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)
        self.assertEqual(len(all_objects), 0)

    def test_new(self):
        """
        Test the 'new' method
        """
        self.storage.new(self.user)
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        all_objects = self.storage.all()
        self.assertIn(key, all_objects)

    def test_save_reload(self):
        """
        Test the 'save' and 'reload' methods
        """
        self.storage.new(self.user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        all_objects = new_storage.all()
        self.assertIn(key, all_objects)

    def test_doc(self):
        self.assertIsNotNone(FileStorage.__doc__)


if __name__ == '__main__':
    unittest.main()
