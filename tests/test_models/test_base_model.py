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
        # Verify that generated IDs are unique in different instances of BaseModel.
        other_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, other_base_model.id)

    def test_id_type(self):
        # Verify that the ID is a string (str).
        self.assertIsInstance(self.base_model.id, str)

    def test_save_updates_date(self):
        # Verify that the 'save' method updates the 'updated_at' date.
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        # Verify the correctness of the 'to_dict' method.
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)
        self.assertEqual(base_model_dict["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"], self.base_model.updated_at.isoformat())

    def test_json_serialization(self):
        # Verify that an object can be converted to JSON and back to an object.
        base_model_dict = self.base_model.to_dict()
        base_model_json = json.dumps(base_model_dict)
        new_base_model_dict = json.loads(base_model_json)
        new_base_model = BaseModel(**new_base_model_dict)
        self.assertEqual(self.base_model.id, new_base_model.id)
        self.assertEqual(self.base_model.created_at, new_base_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_base_model.updated_at)

    def test_instance_creation_with_arguments(self):
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

if __name__ == '__main__':
    unittest.main()
