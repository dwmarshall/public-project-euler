days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 366 % 7  # day of week of 1/1/1901

sundays = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if day % 7 == 0:
            sundays += 1
        day += days_in_month[month]
        if month == 2 and year % 4 == 0:
            day += 1
print(sundays)
