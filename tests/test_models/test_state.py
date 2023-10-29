import unittest
from models.state import State
from models.base_model import BaseModel
import json
from models import storage


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def tearDown(self):
        pass

    def test_state_creation(self):
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_state_serialization(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        new_state = State(**state_dict)
        self.assertEqual(self.state.name, new_state.name)

    def test_doc(self):
        self.assertIsNotNone(State.__doc__)


if __name__ == '__main__':
    unittest.main()
