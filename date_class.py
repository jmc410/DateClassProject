from datetime import date, timedelta
import calendar
# Creation of Date class changing Python-accepted m/d/y order to user-expected order.

class Date:
    """Represent a valid calendar date using datetime.date"""
    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        self.__date = date(year, month, day)
        


    @property
    def month(self):
        """Return stored default month"""
        return self.__date.month

    @property
    def day(self):
        """Property returns stored default day"""
        return self.__date.day

    @property
    def year(self):
        """Property returns stored default year"""
        return self.__date.year

    
    def set_date(self, month, day, year):
        """Allows replacement for the default date to a new one."""
        new_date = date(year, month, day)
        self.__date = new_date

    def is_leap_year(self):
        """Method allow testing for true and false leap years"""
        return calendar.isleap(self.__date.year)

    @staticmethod
    def is_year_leap(year):
        """Standalone static method allows testing for user-input true/false leap years"""
        return calendar.isleap(year)

    def last_day(self):
        """Returns the last day of given month"""
        return calendar.monthrange(self.__date.year, self.__date.month)[1]


    @staticmethod
    def last_day_of_month(month, year):
        """Returns the last day of user-input given month"""
        return calendar.monthrange(year, month)[1]


    def to_numeric_string(self):
        """Returns date in MM/DD/YYYY format."""
        return self.__date.strftime("%m/%d/%Y")

    def to_month_first_string(self):
        """Returns date in Month Day, Year format."""
        return self.__date.strftime("%B %d, %Y")

    def to_day_first_string(self):
        """Returns date in Day Month Year format."""
        return self.__date.strftime("%d %B %Y")



    def __sub__(self, other: object) -> int:
           if not isinstance(other, Date):
                return NotImplemented

           return (self.__date - other.__date).days
    
