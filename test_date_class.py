import unittest
from date_class import Date



class DayTest(unittest.TestCase):
    def test_day(self):
        default_day = Date()
        self.assertEqual(default_day.day,1)

class MonthTest(unittest.TestCase):
    def test_month(self):
        default_month = Date()
        self.assertEqual(default_month.month,1)

class YearTest(unittest.TestCase):
    def test_year(self):
        default_year = Date()
        self.assertEqual(default_year.year,1900)




class ValidDateTest(unittest.TestCase):
    def test_valid(self):
        valid_date = Date(12,25,2026)
        self.assertEqual(valid_date.month, 12)
        self.assertEqual(valid_date.day, 25)
        self.assertEqual(valid_date.year, 2026)

class InvalidDateTest(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(ValueError):
            invalid_date = Date(2,30,1800)


# Testing if default date can be replaced.

class ReplacedDateValid(unittest.TestCase):
    def test_replaced(self):
        replaced_valid = Date()
        replaced_valid.set_date(7,27,2006)
        self.assertEqual(replaced_valid.month,7)
        self.assertEqual(replaced_valid.day,27)
        self.assertEqual(replaced_valid.year,2006)

class ReplacedDateInvalid(unittest.TestCase):
    def test_invalidreplaced(self):
        with self.assertRaises(ValueError):
            replaced_invalid = Date()
            replaced_invalid.set_date(2,31,1800)

        self.assertEqual(replaced_invalid.month,1)
        self.assertEqual(replaced_invalid.day,1)
        self.assertEqual(replaced_invalid.year,1900)

        



# python -m unittest, this is the command to run all unittests. (Use in terminal command line)