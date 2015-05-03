'''
Project Euler Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

  - 1 Jan 1900 was a Monday.
  - Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Answer: 171
https://projecteuler.net/problem=19
'''
#!/usr/bin/python3
def ListBuild():
    ListBuild = [[0,0,0]]
    for year in range(1900, 2001):
        for month in range(1, 13):
            if month in [4, 6, 9, 11]:
                dayRange = 30
            elif not month - 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                        dayRange = 29
                else:
                    dayRange = 28
            else:
                dayRange = 31
            for day in range(1, dayRange + 1):
                ListBuild.append([year, month, day])
    return ListBuild

def sundayList():
    dayList = ListBuild()
    sundayList = []
    for day in range(len(dayList)):
        if not(day - 6) % 7 and dayList[day][0] > 1900 and not dayList[day][2] - 1:
            sundayList.append(dayList[day])
    return len(sundayList)

print(sundayList())
