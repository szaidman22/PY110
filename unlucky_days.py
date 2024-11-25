'''
Some people believe that Fridays that fall on the 13th
day of the month are unlucky days. Write a function that
takes a year as an argument and returns the number of
Friday the 13ths in that year. You may assume that
the year is greater than 1752, which is when the United Kingdom
adopted the modern Gregorian Calendar. You may also assume
that the same calendar will remain in use for the foreseeable future.

Use the datetime.date function to determine whether the 13th of a given month falls on a Friday.
'''
'''
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
'''
'''
input: year integer four digit
output: number of friday the 13ths

algorithm:
1. for month in range(1,13):
    - use datetime.date() and .weekday() method
    - check if that is equal to 4 (friday)
    - if so, increase count by 1
return count
'''
import datetime
print(datetime.date(2024, 1, 22).weekday())

def friday_the_13ths(year):
    spookies = 0
    for month in range(1,13):
        if datetime.date(year, month, 13).weekday() == 4:
            spookies += 1
    
    return spookies


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

