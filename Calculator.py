def get_date(date: str):
    while not date[0].isdigit() or date[0] == '0':
        date = date[1:]
    while not date[-1].isdigit():
        date = date[:-1]
    result, i = [], 0
    while i < len(date):
        if not date[i].isdigit():
            i += 1
            continue
        if len(result) == 3:
            raise ValueError('Invalid date!')
        res = ''
        while date[i].isdigit():
            res += date[i]
            i += 1
            if i == len(date):
                break
        result.append(int(res))
        i += 1
    if not result:
        return [1, 1, 2000]
    if len(result) == 1:
        return [1, 1] + result
    if len(result) == 2:
        return result + [2000]
    return result
def leap(y: int):
    return not bool(y % 4) and (bool(y % 100) or not bool(y % 400))
def month_days(m: int, y: int):
    return 30 + (m > 7) + (-1) ** (m > 7) * (m % 2) if m != 2 else 28 + leap(y)
def fake_date(d: int, m: int, y: int):
    return d not in range(1, month_days(m, y) + 1) or m not in range(1, 13)
Weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if __name__ == '__main__':
    breaker, beginning_date, ending_date, last_date, days = False, get_date(input('Beginning date (day:month:year): ')), [], input('Ending date (day:month:year): '), 0
    year = beginning_date[2]
    Jan_1_weekday = year - 1 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    if last_date:
        ending_date = get_date(last_date)
    else:
        ending_date = [1, 1, year + 1]
    if fake_date(*beginning_date) or fake_date(*ending_date):
        raise ValueError('Invalid date!')
    elif year > ending_date[2] or year == ending_date[2] and (beginning_date[1] > ending_date[1] or beginning_date[1] == ending_date[1] and beginning_date[0] > ending_date[0]):
        if leap(year):
            Jan_1_weekday += 1
        while not breaker:
            for month in range(12, 0, -1):
                for day in range(month_days(month, year), 0, -1):
                    if year == beginning_date[2] and (month == beginning_date[1] and day <= beginning_date[0] or month < beginning_date[1]) or year < beginning_date[2]:
                        days += 1
                        print(f'{day:02d}:{month:02d}:{year} - {Weekdays[Jan_1_weekday % 7]} - {days}')
                        if [day, month, year] == ending_date:
                            breaker = True
                            break
                    Jan_1_weekday -= 1
                if breaker:
                    break
            year -= 1
    else:
        while not breaker:
            for month in range(1, 13):
                for day in range(1, month_days(month, year) + 1):
                    if year == beginning_date[2] and (month == beginning_date[1] and day >= beginning_date[0] or month > beginning_date[1]) or year > beginning_date[2]:
                        days += 1
                        if last_date == '' or beginning_date == ending_date:
                            print(Weekdays[Jan_1_weekday % 7])
                            breaker = True
                            break
                        print(f'{day:02d}:{month:02d}:{year} - {Weekdays[Jan_1_weekday % 7]} - {days}')
                        if [day, month, year] == ending_date:
                            breaker = True
                            break
                    Jan_1_weekday += 1
                if breaker:
                    break
            year += 1