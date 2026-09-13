import unittest
from date_class import Date



class DayTest(unittest.TestCase):
    def test_day(self):
        default_day = Date()
        self.assertEqual(default_day.day,1)


# python -m unittest, this is the command to run all unittests. (Use in terminal command line)