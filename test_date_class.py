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



# python -m unittest, this is the command to run all unittests. (Use in terminal command line)