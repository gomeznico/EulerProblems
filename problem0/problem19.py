"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
## could use Datetime module to iterate through every day and add a counter.
## start with that

import datetime

monday = datetime.date(1900,1,1)
start = datetime.date(1901,1,6) # first sunday of 1901 was the 6th
end = datetime.date(2000,12,2)
week = datetime.timedelta(7)

today = start
seen_sundays = 0
while today < end:
    if today.day == 1 and today.weekday() == 6:
        seen_sundays+=1
        # print(today)
    today += week
# print(seen_sundays)   # 171

"""
1901-09-01
1901-12-01
1902-06-01
1903-02-01
1903-03-01
1903-11-01
1904-05-01
1905-01-01
1905-10-01
1906-04-01
1906-07-01
1907-09-01
1907-12-01
1908-03-01
1908-11-01
1909-08-01
1910-05-01
1911-01-01
1911-10-01
1912-09-01
1912-12-01
1913-06-01
1914-02-01
1914-03-01
1914-11-01
1915-08-01
1916-10-01
1917-04-01
1917-07-01
1918-09-01
1918-12-01
1919-06-01
1920-02-01
1920-08-01
1921-05-01
1922-01-01
1922-10-01
1923-04-01
1923-07-01
1924-06-01
1925-02-01
1925-03-01
1925-11-01
1926-08-01
1927-05-01
1928-01-01
1928-04-01
1928-07-01
1929-09-01
1929-12-01
1930-06-01
1931-02-01
1931-03-01
1931-11-01
1932-05-01
1933-01-01
1933-10-01
1934-04-01
1934-07-01
1935-09-01
1935-12-01
1936-03-01
1936-11-01
1937-08-01
1938-05-01
1939-01-01
1939-10-01
1940-09-01
1940-12-01
1941-06-01
1942-02-01
1942-03-01
1942-11-01
1943-08-01
1944-10-01
1945-04-01
1945-07-01
1946-09-01
1946-12-01
1947-06-01
1948-02-01
1948-08-01
1949-05-01
1950-01-01
1950-10-01
1951-04-01
1951-07-01
1952-06-01
1953-02-01
1953-03-01
1953-11-01
1954-08-01
1955-05-01
1956-01-01
1956-04-01
1956-07-01
1957-09-01
1957-12-01
1958-06-01
1959-02-01
1959-03-01
1959-11-01
1960-05-01
1961-01-01
1961-10-01
1962-04-01
1962-07-01
1963-09-01
1963-12-01
1964-03-01
1964-11-01
1965-08-01
1966-05-01
1967-01-01
1967-10-01
1968-09-01
1968-12-01
1969-06-01
1970-02-01
1970-03-01
1970-11-01
1971-08-01
1972-10-01
1973-04-01
1973-07-01
1974-09-01
1974-12-01
1975-06-01
1976-02-01
1976-08-01
1977-05-01
1978-01-01
1978-10-01
1979-04-01
1979-07-01
1980-06-01
1981-02-01
1981-03-01
1981-11-01
1982-08-01
1983-05-01
1984-01-01
1984-04-01
1984-07-01
1985-09-01
1985-12-01
1986-06-01
1987-02-01
1987-03-01
1987-11-01
1988-05-01
1989-01-01
1989-10-01
1990-04-01
1990-07-01
1991-09-01
1991-12-01
1992-03-01
1992-11-01
1993-08-01
1994-05-01
1995-01-01
1995-10-01
1996-09-01
1996-12-01
1997-06-01
1998-02-01
1998-03-01
1998-11-01
1999-08-01
2000-10-01
"""

# custom soln
# Jan Feb Mar Apr May Jun jul aug sept oct nov dec
months =      [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 365 days
leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 366 days

first_day_of_month = []
first_day_of_leap_month = []

for i,days in enumerate(months):
    add = sum(months[0:i])
    first_day_of_month.append(add)
for i,days in enumerate(leap_months):
    add = sum(leap_months[0:i])
    first_day_of_leap_month.append(add)
# print(first_day_of_month)
# print(first_day_of_leap_month)

today = [1901,5]    # first sunday is on the 5th day of year (0 indexed)
sundays = 0

def is_leap_year(year):
    if year%400 == 0: return True
    if year%4 == 0 and year%100 != 0:
        return True
    return False

while today[0]<2001:
    year = today[0]
    day = today[1]
    first_days = first_day_of_month
    days_in_year = 365
    if is_leap_year(year):
        first_days = first_day_of_leap_month
        days_in_year = 366
    if day in first_days:
        sundays+=1
        # print(today)
    today[1] +=7
    if today[1]>=days_in_year:
        today[1] = today[1]%days_in_year
        today[0] +=1
print(today)
print(sundays)








