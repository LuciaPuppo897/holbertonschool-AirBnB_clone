import unittest
from models.state import State
from datetime import datetime
import json
import os
from models import storage

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_state_creation(self):
        # Verify that a State is created correctly
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_state_serialization(self):
        # Verify if the state can be serialized and deserialized
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        new_state = State(**state_dict)
        self.assertEqual(self.state.name, new_state.name)

    def test_state_storage(self):
        storage.new(self.state)
        storage.save()
        # Check if the State is stored correctly in FileStorage
        self.assertIn(self.state, storage.all(State))

if __name__ == '__main__':
    unittest.main()
