#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(22).__nb_instances)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_float_id(self):
        self.assertEqual(7.5, Base(7.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_str_id(self):
        self.assertEqual("string", Base("string").id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_list_id(self):
        self.assertEqual([11, 12, 13], Base([11, 12, 13]).id)

    def test_tuple_id(self):
        self.assertEqual((4, 5), Base((4, 5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(10), Base(range(10)).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_types(self):
        r = Rectangle(10, 7, 2, 8, 6)
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_rectangle_length(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        one_dict_length = len(Base.to_json_string([Rectangle(10, 7, 2, 8, 6).to_dictionary()]))
        two_dicts_length = len(Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()]))
        self.assertGreater(one_dict_length, 0)
        self.assertGreater(two_dicts_length, one_dict_length)

    def test_to_json_string_square_length(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        one_dict_length = len(Base.to_json_string([Square(10, 2, 3, 4).to_dictionary()]))
        two_dicts_length = len(Base.to_json_string([s1.to_dictionary(), s2.to_dictionary()]))
        self.assertGreater(one_dict_length, 0)
        self.assertGreater(two_dicts_length, one_dict_length)

    def test_to_json_string_empty_list_and_none(self):
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_invalid_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    class TestBase_save_to_file(unittest.TestCase):
        """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Clean up any created files."""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(filename)
            except IOError:
                pass

    def test_save_to_file_types(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        self._test_save_to_file(r1, "Rectangle.json", 53)
        self._test_save_to_file([r1, r2], "Rectangle.json", 105)
        self._test_save_to_file(s1, "Square.json", 39)
        self._test_save_to_file([s1, s2], "Square.json", 77)

    def test_save_to_file_base_class(self):
        s = Square(10, 7, 2, 8)
        self._test_save_to_file(s, "Base.json", 39)

    def test_save_to_file_overwrite(self):
        s1 = Square(9, 2, 39, 2)
        s2 = Square(10, 7, 2, 8)
        self._test_save_to_file(s1, "Square.json", 39)
        self._test_save_to_file(s2, "Square.json", 39)

    def test_save_to_file_empty_and_none(self):
        self._test_save_to_file(None, "Square.json", "[]")
        self._test_save_to_file([], "Square.json", "[]")

    def test_save_to_file_invalid_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def _test_save_to_file(self, obj, filename, expected_length):
        obj_class = obj.__class__
        obj_class.save_to_file([obj])
        with open(filename, "r") as f:
            self.assertEqual(len(f.read()), expected_length)

    class TestBase_from_json_string(unittest.TestCase):
        """Unittests for testing from_json_string method of Base class."""

    def test_type_and_single_object(self):
        # Combine type check and single object test for conciseness
        obj = Rectangle(id=89, width=10, height=4)
        json_str = Rectangle.to_json_string([obj])
        objects = Base.from_json_string(json_str)
        self.assertEqual(list, type(objects))
        self.assertEqual(obj, objects[0])

    def test_multiple_objects(self):
        obj1 = Rectangle(id=89, width=10, height=4, x=7, y=8)
        obj2 = Rectangle(id=98, width=5, height=2, x=1, y=3)
        expected_list = [obj1, obj2]
        json_str = Rectangle.to_json_string(expected_list)
        objects = Base.from_json_string(json_str)
        self.assertEqual(expected_list, objects)

    def test_square_objects(self):
        obj1 = Square(id=89, size=10, height=4)
        obj2 = Square(id=7, size=1, height=7)
        expected_list = [obj1, obj2]
        json_str = Square.to_json_string(expected_list)
        objects = Base.from_json_string(json_str)
        self.assertEqual(expected_list, objects)

    def test_empty_and_none(self):
        # Combine empty list and None tests for conciseness
        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string("[]"))

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    class TestBase_create(unittest.TestCase):
        """Unittests for testing create method of Base class."""

    def test_create_rectangle_properties(self):
        r1_dict = {"id": 1, "width": 3, "height": 5, "x": 1, "y": 2, "type": "Rectangle"}
        r1 = Rectangle.create(**r1_dict)
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square_properties(self):
        s1_dict = {"id": 1, "size": 4, "x": 3, "y": 1, "type": "Square"}
        s1 = Square.create(**s1_dict)
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_create_invalid_type(self):
        invalid_dict = {"invalid_type": True}
        with self.assertRaises(ValueError):
            Base.create(**invalid_dict)

    class TestBase_load_from_file(unittest.TestCase):
        """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Clean up any created files."""
        for filename in ["Rectangle.json", "Square.json"]:
            try:
                os.remove(filename)
            except IOError:
                pass

    def test_load_from_file_types_and_order(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Base.save_to_file([r1, r2, s1, s2])
        output = Base.load_from_file()
        self.assertEqual(2, len(output))
        self.assertEqual(type(output[0]), type(r1))
        self.assertEqual(type(output[1]), type(s1))
        self.assertEqual(str(r1), str(output[0]))
        self.assertEqual(str(s1), str(output[1]))

    def test_load_from_file_empty_file(self):
        output = Rectangle.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_invalid_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    class TestBase_save_to_file_csv(unittest.TestCase):
        """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Clean up any created files."""
        for filename in ["Rectangle.csv", "Square.csv", "Base.csv"]:
            try:
                os.remove(filename)
            except IOError:
                pass

    def test_save_to_file_csv_types(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        self._test_save_to_file_csv(r1, "Rectangle.csv", "5,10,7,2,8")
        self._test_save_to_file_csv([r1, r2], "Rectangle.csv", "5,10,7,2,8\n2,4,1,2,3")
        self._test_save_to_file_csv(s1, "Square.csv", "8,10,7,2")
        self._test_save_to_file_csv([s1, s2], "Square.csv", "8,10,7,2\n3,8,1,2")

    def test_save_to_file_csv_base_class(self):
        s = Square(10, 7, 2, 8)
        self._test_save_to_file_csv(s, "Base.csv", "8,10,7,2")

    def test_save_to_file_csv_overwrite(self):
        s1 = Square(9, 2, 39, 2)
        s2 = Square(10, 7, 2, 8)
        self._test_save_to_file_csv(s1, "Square.csv", "8,10,7,2")

    def test_save_to_file_csv_empty_and_none(self):
        self._test_save_to_file_csv(None, "Square.csv", "")
        self._test_save_to_file_csv([], "Square.csv", "")

    def test_save_to_file_csv_invalid_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    def _test_save_to_file_csv(self, obj, filename, expected_content):
        obj_class = obj.__class__
        obj_class.save_to_file_csv([obj])
        with open(filename, "r") as f:
            self.assertEqual(f.read(), expected_content)

    if __name__ == "__main__":
        unittest.main()
