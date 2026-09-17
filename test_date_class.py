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

class InvalidDateTestYear(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(ValueError):
            invalid_date_year = Date(2,25,0)

class InvalidDateTestMonth(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(ValueError):
            invalid_date_month = Date(13,1,2000)

class InvalidDateTestDay(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(ValueError):
            invalid_date_day = Date(2,30,1800)


class InvalidLeapDay(unittest.TestCase):
    def test_invalid_leap_day(self):
        with self.assertRaises(ValueError):
            invalid_leap_day = Date(2,29,2023)

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


class LeapYearTest(unittest.TestCase):
    def test_leapyearmethod(self):
        leap_year = Date(12,12,2024)
        self.assertEqual(leap_year.is_leap_year(),True)

class NotLeapYearTest(unittest.TestCase):
    def test_notleapyearmethod(self):
        not_leap_year = Date(12,12,2023)
        self.assertEqual(not_leap_year.is_leap_year(),False)


class StaticLeapYearTest(unittest.TestCase):
    def test_staticleapyear(self):
        static_leap = Date.is_year_leap(2024)
        self.assertEqual(static_leap,True)


class StaticNotLeapYearTest(unittest.TestCase):
    def test_staticnotleapyear(self):
        static_notleap = Date.is_year_leap(2023)
        self.assertEqual(static_notleap,False)

class LastDayTest(unittest.TestCase):
    def test_lastday(self):
        last_day_test = Date(2,2,2024)
        self.assertEqual(last_day_test.last_day(),29)

class StaticLastDay(unittest.TestCase):
    def test_staticlastday(self):
        static_lastday = Date.last_day_of_month(2,2023)
        self.assertEqual(static_lastday,28)


class NumericFormat(unittest.TestCase):
    def test_numformat(self):
        numeric_format = Date(12,25,2021)
        numeric_format = numeric_format.to_numeric_string()
        self.assertEqual(numeric_format,"12/25/2021")


class MonthFirstString(unittest.TestCase):
    def test_monthfirst(self):
        month_first = Date(12,25,2021)
        month_first = month_first.to_month_first_string()
        self.assertEqual(month_first,"December 25, 2021")


class DayFirstString(unittest.TestCase):
    def test_dayfirst(self):
        day_first = Date(12,25,2021)
        day_first = day_first.to_day_first_string()
        self.assertEqual(day_first,"25 December 2021")


class Subtraction(unittest.TestCase):
    def test_subtraction(self):
        day1 = Date(4,18,2024)
        day2 = Date(4,10,2024)
        difference = day1 - day2
        self.assertEqual(difference,8)

class NegativeSubtraction(unittest.TestCase):
    def test_negativesubtraction(self):
        nday1 = Date(11,10,2003)
        nday2 = Date(2,2,2006)
        ndifference = nday1 - nday2
        self.assertEqual(ndifference,-815)
# python -m unittest, this is the command to run all unittests. (Use in terminal command line)