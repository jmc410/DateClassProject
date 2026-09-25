import unittest
from date_class import Date
from unittest.mock import patch





class UserInput(unittest.TestCase):
    @patch("builtins.input", side_effect=["4", "18", "2018"])
    def test_from_input_creates_date(self, mock_input):

        result = Date.from_input()

        self.assertEqual(result.month, 4)
        self.assertEqual(result.day, 18)
        self.assertEqual(result.year, 2018)


    @patch("builtins.input", side_effect=["13", "18", "2018"])
    def test_from_input_creates_date(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["4", "35", "2018"])
    def test_from_input_creates_date(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["2", "29", "2003"])
    def test_from_input_creates_date(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()


    @patch("builtins.input", side_effect=["a", "b", "c"])
    def test_from_input_creates_date(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()


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


# Other subtraction test

class Subtraction(unittest.TestCase):
    def test_subtraction(self):
        day1 = Date(2,2,2006)
        day2 = Date(11,10,2003)
        difference = day1 - day2
        self.assertEqual(difference,815)



class NegativeSubtraction(unittest.TestCase):
    def test_negativesubtraction(self):
        nday1 = Date(11,10,2003)
        nday2 = Date(2,2,2006)
        ndifference = nday1 - nday2
        self.assertEqual(ndifference,-815)


class EqualSubtraction(unittest.TestCase):
    def test_negativesubtraction(self):
        eday1 = Date(11,10,2003)
        eday2 = Date(11,10,2003)
        edifference = eday1 - eday2
        self.assertEqual(edifference,0)



# Starting increment testing.


class IncrementTest1(unittest.TestCase):
    def test_increment(self):
        test1 = Date(4,30,2000)

        returned_date = test1.increment()

        self.assertEqual(test1.day, 1)
        self.assertEqual(test1.month, 5)
        self.assertEqual(test1.year, 2000)

        self.assertIs(returned_date,test1)


class IncrementTest2(unittest.TestCase):
    def test_increment(self):
        test1 = Date(1,31,2000)

        returned_date = test1.increment()

        self.assertEqual(test1.day, 1)
        self.assertEqual(test1.month, 2)
        self.assertEqual(test1.year, 2000)

        self.assertIs(returned_date,test1)


class IncrementTest3(unittest.TestCase):
    def test_increment(self):
        test1 = Date(2,28,2003)

        returned_date = test1.increment()

        self.assertEqual(test1.day, 1)
        self.assertEqual(test1.month, 3)
        self.assertEqual(test1.year, 2003)

        self.assertIs(returned_date,test1)


class IncrementTest4(unittest.TestCase):
    def test_increment(self):
        test1 = Date(2,28,2004)

        returned_date = test1.increment()

        self.assertEqual(test1.day, 29)
        self.assertEqual(test1.month, 2)
        self.assertEqual(test1.year, 2004)

        self.assertIs(returned_date,test1)



class IncrementTest5(unittest.TestCase):
    def test_increment(self):
        test1 = Date(12,31,2003)

        returned_date = test1.increment()

        self.assertEqual(test1.day, 1)
        self.assertEqual(test1.month, 1)
        self.assertEqual(test1.year, 2004)

        self.assertIs(returned_date,test1)






class DeincrementTest(unittest.TestCase):
    def test_deincrement(self):
        test1 = Date(4,30,2000)

        returned_date = test1.decrement()

        self.assertEqual(test1.day, 29)
        self.assertEqual(test1.month, 4)
        self.assertEqual(test1.year, 2000)

        self.assertIs(returned_date,test1)



class DeincrementTest2(unittest.TestCase):
    def test_deincrement(self):
        test1 = Date(5,1,2000)

        returned_date = test1.decrement()

        self.assertEqual(test1.day, 30)
        self.assertEqual(test1.month, 4)
        self.assertEqual(test1.year, 2000)

        self.assertIs(returned_date,test1)

class DeincrementTest3(unittest.TestCase):
    def test_deincrement(self):
        test1 = Date(3,1,2003)

        returned_date = test1.decrement()

        self.assertEqual(test1.day, 28)
        self.assertEqual(test1.month, 2)
        self.assertEqual(test1.year, 2003)

        self.assertIs(returned_date,test1)

class DeincrementTest4(unittest.TestCase):
    def test_deincrement(self):
        test1 = Date(3,1,2004)

        returned_date = test1.decrement()

        self.assertEqual(test1.day, 29)
        self.assertEqual(test1.month, 2)
        self.assertEqual(test1.year, 2004)

        self.assertIs(returned_date,test1)


class DeincrementTest5(unittest.TestCase):
    def test_deincrement(self):
        test1 = Date(1,1,2003)

        returned_date = test1.decrement()

        self.assertEqual(test1.day, 31)
        self.assertEqual(test1.month, 12)
        self.assertEqual(test1.year, 2002)

        self.assertIs(returned_date,test1)



class StringTest(unittest.TestCase):
    def test_stringtest(self):
        strtest = str(Date(4,18,2018))
        self.assertEqual(strtest,"April 18, 2018")

class StringTest2(unittest.TestCase):
    def test_stringtest(self):
        strtest = str(Date(4,8,2018))
        self.assertEqual(strtest,"April 8, 2018")


class StringTest3(unittest.TestCase):
    def test_stringtest(self):
        strtest = str(Date(2,29,2004))
        self.assertEqual(strtest,"February 29, 2004")
        


class StringTestBoundary1(unittest.TestCase):
    def test_stringtest(self):
        strtest = str(Date(12,31,2004))
        self.assertEqual(strtest,"December 31, 2004")


class StringTestBoundary2(unittest.TestCase):
    def test_stringtest(self):
        strtest = str(Date(1,1,2005))
        self.assertEqual(strtest,"January 1, 2005")


# python -m unittest, this is the command to run all unittests. (Use in terminal command line)