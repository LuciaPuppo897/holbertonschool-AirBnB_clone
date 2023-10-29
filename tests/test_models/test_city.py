import unittest
from models.city import City
from models import storage
from datetime import datetime
import json
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_city_creation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes(self):
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_str_method(self):
        city = City()
        self.assertIsInstance(str(city), str)

    def test_id_correct(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_save_method(self):
        city = City()
        original_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(original_updated_at, city.updated_at)

    def test_subclass_check(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_doc(self):
        self.assertIsNotNone(City.__doc__)


if __name__ == '__main__':
    unittest.main()
