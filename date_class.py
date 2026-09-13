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
        