from Personal.Calendar.Calculator import month_days
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.__month = max(min(month, 12), 1)
        self.__year = year
        self.__day = max(min(day, month_days(self.__month, self.__year)), 1)
    def weekday(self):
        from Personal.Calendar.Calculator import Weekdays
        jan_1_weekday = self.__year - 1 + (self.__year - 1) // 4 - (self.__year - 1) // 100 + (self.__year - 1) // 400
        month = 1
        while month < self.__month:
            jan_1_weekday += month_days(month, self.__year) - 28
            month += 1
        return Weekdays[(jan_1_weekday + self.__day - 1) % 7]
    def tomorrow(self):
        day, month, year = self.__day, self.__month, self.__year
        day += 1
        if day > month_days(month, year):
            day = 1
            month += 1
            if month == 13:
                year += 1
                month = 1
        return Date(day, month, year)
    def yesterday(self):
        day, month, year = self.__day, self.__month, self.__year
        day -= 1
        if not day:
            month -= 1
            if not month:
                month = 12
                year -= 1
            day = month_days(month, year)
        return Date(day, month, year)
    def copy(self):
        return Date(self.__day, self.__month, self.__year)
    def __add__(self, other):
        if isinstance(other, int):
            res = self.copy()
            if other < 0:
                return res - -other
            for _ in range(other):
                res = res.tomorrow()
            return res
        raise TypeError(f'Addition not defined between type Date and type {type(other)}!')
    def __sub__(self, other):
        if isinstance(other, int):
            res = self.copy()
            if other < 0:
                return res + -other
            for _ in range(other):
                res = res.yesterday()
            return res
        raise TypeError(f'Subtraction not defined between type Date and type {type(other)}!')
    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.__day, self.__month, self.__year) == (other.__day, other.__month, other.__year)
        return False
    def __lt__(self, other):
        if isinstance(other, Date):
            return (self.__year, self.__month, self.__day) < (other.__year, other.__month, other.__day)
    def __le__(self, other):
        if isinstance(other, Date):
            return (self.__year, self.__month, self.__day) <= (other.__year, other.__month, other.__day)
    def __str__(self):
        return f'{self.__day:02d}:{self.__month:02d}:{self.__year}'
    def __repr__(self):
        return str(self)
