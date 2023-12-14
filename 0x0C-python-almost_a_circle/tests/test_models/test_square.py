#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_square_initialization(self):
        """Test the square initialization."""
        square = Square(10, 3, 4)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_invalid_size_value(self):
        """Test raising TypeError for invalid size."""
        with self.assertRaises(TypeError):
            Square("invalid", 3, 4)

    def test_invalid_size_range(self):
        """Test raising ValueError for size <= 0."""
        with self.assertRaises(ValueError):
            Square(0, 3, 4)

    def test_square_area_calculation(self):
        """Test the area calculation method for square."""
        square = Square(10)
        self.assertEqual(square.area(), 100)
