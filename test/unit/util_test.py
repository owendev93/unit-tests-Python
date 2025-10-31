import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    def test_convert_to_number_with_floats(self):
        self.assertAlmostEqual(3.14, util.convert_to_number("3.14"), delta=0.0000001)
        self.assertAlmostEqual(-2.5, util.convert_to_number("-2.5"), delta=0.0000001)
        self.assertAlmostEqual(0.001, util.convert_to_number("0.001"), delta=0.0000001)

    def test_convert_to_number_with_negative_integers(self):
        self.assertEqual(-5, util.convert_to_number("-5"))
        self.assertEqual(-100, util.convert_to_number("-100"))
        self.assertEqual(-1, util.convert_to_number("-1"))

    def test_validate_permissions_user1(self):
        self.assertTrue(util.validate_permissions("2 * 2", "user1"))
        self.assertTrue(util.validate_permissions("any operation", "user1"))

    def test_validate_permissions_other_user(self):
        self.assertFalse(util.validate_permissions("2 * 2", "user2"))
        self.assertFalse(util.validate_permissions("any operation", "other"))
        self.assertFalse(util.validate_permissions("test", "admin"))
