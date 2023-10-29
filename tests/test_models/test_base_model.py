#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        pass

    def test_instance_creation(self):
        self.assertIsInstance(self.base_model, BaseModel)

    def test_unique_ids(self):
        base_model = BaseModel()
        other = BaseModel()
        self.assertNotEqual(base_model.id, other.id)

    def test_instance_creation_time(self):
        base_model = BaseModel()
        other_base_model = BaseModel()
        self.assertNotEqual(base_model.created_at, other_base_model.created_at)

    def test_id_type(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_date(self):
        original = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original, self.base_model.updated_at)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)
        self.assertEqual(base_model_dict["created_at"],
                         self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                         self.base_model.updated_at.isoformat())

    def test_save_method(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_create_with_args(self):
        data = {
            'id': 'test_id',
            'created_at': '2023-10-26T12:00:00.000000',
            'updated_at': '2023-10-26T13:00:00.000000',
            'custom_attribute': 'custom_value'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, 'test_id')
        self.assertEqual(obj.created_at.isoformat(), '2023-10-26T12:00:00')
        self.assertEqual(obj.updated_at.isoformat(), '2023-10-26T13:00:00')
        self.assertEqual(obj.custom_attribute, 'custom_value')

    def test_create_without_args(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_id_lenght(self):
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertEqual(len(base.id), 36)

    def test_doc(self):
        self.assertIsNotNone(BaseModel.__doc__)


if __name__ == '__main__':
    unittest.main()
