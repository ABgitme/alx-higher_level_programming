#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_rectangle_initialization(self):
        """Test the rectangle initialization."""
        rectangle = Rectangle(10, 20, 3, 4)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_invalid_width_value(self):
        """Test raising TypeError for invalid width."""
        with self.assertRaises(TypeError):
            Rectangle("invalid", 20, 3, 4)

    def test_invalid_height_value(self):
        """Test raising TypeError for invalid height."""
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid", 3, 4)

    def test_invalid_width_range(self):
        """Test raising ValueError for width <= 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 3, 4)

    def test_invalid_height_range(self):
        """Test raising ValueError for height <= 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 3, 4)

    def test_area_calculation(self):
        """Test the area calculation method."""
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.area(), 200)

    def test_perimeter_calculation(self):
        """Test the perimeter calculation method."""
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.perimeter(), 60)

    def test_str_representation(self):
        """Test the string representation method."""
        rectangle = Rectangle(10, 20, 1, 2)
        expected_str = "[Rectangle] (1) 1/2 - 10/20"
        self.assertEqual(str(rectangle), expected_str)