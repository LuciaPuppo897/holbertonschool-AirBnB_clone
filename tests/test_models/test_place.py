import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
import json


class TestPlaceAttributes(unittest.TestCase):
    def test_default_attributes(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_custom_attributes(self):
        place = Place(city_id="1", user_id="2", name="Test Place",
                      description="This is a test place", number_rooms=3,
                      number_bathrooms=2, max_guest=6, price_by_night=100,
                      latitude=40.7128, longitude=-74.0060, amenity_ids=[1, 2])
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "This is a test place")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, [1, 2])

    def test_from_dict(self):
        place_data = {
            "city_id": "1",
            "user_id": "2",
            "name": "Test Place",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "max_guest": 6
        }
        place = Place(**place_data)
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)

    def test_int_attributes(self):
        place = Place()
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)

    def test_float_attributes(self):
        place = Place()
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)

    def test_str_attributes(self):
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)

    def test_diff_id(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_save_method(self):
        place = Place()
        original = place.updated_at
        place.save()
        self.assertNotEqual(original, place.updated_at)

    def test_subclass_check(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_str_method(self):
        place = Place()
        self.assertIsInstance(str(place), str)

    def test_doc(self):
        self.assertIsNotNone(Place.__doc__)


if __name__ == '__main__':
    unittest.main()
