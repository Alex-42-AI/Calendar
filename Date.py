from Personal.Calendar.Calculator import month_days
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.__month = max(min(month, 12), 0)
        self.__year = year
        self.__day = max(min(day, month_days(self.__month, self.__year)), 0)
    def weekday(self):
        from Personal.Calendar.Calculator import Weekdays
        jan_1_weekday = self.__year - 1 + (self.__year - 1) // 4 - (self.__year - 1) // 100 + (self.__year - 1) // 400
        month, day = 1, 1
        while month < self.__month:
            jan_1_weekday += month_days(month, self.__year) - 28
            month += 1
        while day < self.__day:
            jan_1_weekday += 1
            day += 1
        return Weekdays[jan_1_weekday % 7]
    def tomorrow(self):
        self.__day += 1
        if self.__day > month_days(self.__month, self.__year):
            self.__day = 1
            self.__month += 1
            if self.__month == 13:
                self.__year += 1
                self.__month = 1
        return self
    def yesterday(self):
        self.__day -= 1
        if not self.__day:
            self.__month -= 1
            if not self.__month:
                self.__month = 12
                self.__year -= 1
            self.__day = month_days(self.__month, self.__year)
        return self
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
            return (self.__day, self.__month, self.__year) < (other.__day, other.__month, other.__year)
    def __le__(self, other):
        if isinstance(other, Date):
            return (self.__day, self.__month, self.__year) <= (other.__day, other.__month, other.__year)
    def __str__(self):
        return f'{self.__day:02d}:{self.__month:02d}:{self.__year}'
    def __repr__(self):
        return str(self)