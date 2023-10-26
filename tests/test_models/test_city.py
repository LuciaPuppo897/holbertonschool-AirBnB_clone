import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
from datetime import datetime
import json
import os

class TestCity(unittest.TestCase):
    def setUp(self):
        # Set up the test environment here if needed
        pass

    def tearDown(self):
        # Clean up the test environment here if needed
        pass

    def test_user_creation(self):
        # Verify that city is created correctly
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id)
        self.assertEqual(city.name)
        
    def test_user_serialization(self):
        # Verify if the city can be serialized and deserialized
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        new_city = City(**city.to_dict)
        self.assertEqual(city.state_id)
        self.assertEqual(city.name)

    def test_user_storage(self):
        city = City()
        storage.new(city)
        storage.save()
        # Check if User is stored correctly in FileStorage
        self.assertIn(city, storage.all(City))

if __name__ == '__main__':
    unittest.main()
