import unittest
from models.user import User
from console import HBNBCommand
from datetime import datetime
import json


class TestConsole(unittest.TestCase):

    def test_doc(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
