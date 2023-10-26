##!/usr/bin/python3
""" Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_unique_ids(self):
        # Check that generated IDs are unique
        other_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, other_base_model.id)

    def test_id_type(self):
        # Check that the ID is a string
        self.assertIsInstance(self.base_model.id, str)


    def test_save_updates_date(self):
        # Check that the 'save' method updates the updated_at attribute
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        # Check the correctness of the 'to_dict' method
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)
        self.assertEqual(base_model_dict["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"], self.base_model.updated_at.isoformat())

    def test_json_serialization(self):
        # Check if object can be converted to JSON and back
        base_model_dict = self.base_model.to_dict()
        base_model_json = json.dumps(base_model_dict)
        new_base_model_dict = json.loads(base_model_json)
        new_base_model = BaseModel(**new_base_model_dict)
        self.assertEqual(self.base_model.id, new_base_model.id)
        self.assertEqual(self.base_model.created_at, new_base_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_base_model.updated_at)


