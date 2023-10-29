import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import json
from models import storage


class TestAmenity(unittest.TestCase):

    def test_amenity_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes(self):
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_amenity_to_dict(self):
        amenity = Amenity()
        amenity.name = "Parking"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "Parking")

    def test_amenity_from_dict(self):
        data = {
            "id": "test_id",
            "created_at": "2023-10-26T12:00:00.000000",
            "updated_at": "2023-10-26T13:00:00.000000",
            "name": "Gym"
        }
        amenity = Amenity(**data)
        self.assertEqual(amenity.name, "Gym")

    def test_str_amenity(self):
        obj = Amenity()
        obj.id = "345"
        obj_str = obj.__str__()
        self.assertIn("[Amenity] (234)", obj_str)

    def test_receive_nothing(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_correctness(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_save_method(self):
        amenity = Amenity()
        original = amenity.updated_at
        amenity.save()
        self.assertNotEqual(original, amenity.updated_at)

    def test_subclass_check(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_doc(self):
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == '__main__':
    unittest.main()
