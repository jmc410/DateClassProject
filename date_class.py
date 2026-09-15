from datetime import date
import calendar

class Date:
    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        self.__date = date(year, month, day)
        
    @property
    def month(self):
        return self.__date.month

    @property
    def day(self):
        return self.__date.day

    @property
    def year(self):
        return self.__date.year
    
    def set_date(self, month, day, year):
        new_date = date(year, month, day)
        self.__date = new_date


    def true_is_leap_year(self):
        return calendar.isleap(self.__date.year)

    def false_is_leap_year(self):
        return calendar.isleap(self.__date.year)


    @staticmethod
    def is_year_leap(year):
        return calendar.isleap(year)

    @staticmethod
    def is_false_year_leap(year):
        return calendar.isleap(year)


    def last_day(self):
        return calendar.monthrange(self.__date.year,self.__date.month)[1]


    def last_day_nonleap(self):
        return calendar.monthrange(self.__date.year,self.__date.month)[1]

    @staticmethod
    def last_day_of_month(month,year):
        return calendar.monthrange(year,month)[1]


    def to_numeric_string(self):
        return self.__date.strftime("%m/%d/%Y")

    def to_month_first_string(self):
        return self._date.strftime("%B %d/%Y")