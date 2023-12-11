#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_assignment(self):
        """Test if the id is assigned correctly."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)
        base2 = Base(5)
        self.assertEqual(base2.id, 5)

    def test_id_None(self):
        """Test when id is None."""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_public(self):
        b = Base(10)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        base = Base(12, 3, 4)
        expected_dict = {
            "id": 12,
            "width": 3,
            "height": 4,
            "x": 0,
            "y": 0,
        }
        self.assertEqual(base.to_dictionary(), expected_dict)