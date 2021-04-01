"""
https://leetcode.com/problems/day-of-the-week/
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.



Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"


Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""


# Runtime: 32 ms, faster than 54.12% of Python3 online submissions for Day of the Week.
# Memory Usage: 14.2 MB, less than 82.16% of Python3 online submissions for Day of the Week.
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        dayofWeekNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        def isLeap(year: int) -> bool:
            return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

        def daysInYear(year: int) -> int:
            return 366 if isLeap(year) else 365

        def daysInMonth(month: int, year: int) -> int:
            if month == 2:
                return 29 if isLeap(year) else 28
            elif month in [4, 6, 9, 11]:
                return 30
            else:
                return 31

        dow = 5  # 1-jan-1971
        for y in range(1971, year):
            dow += daysInYear(y)
            dow %= 7
        for m in range(1, month):
            dow += daysInMonth(m, year)
        dow += day-1
        dow %= 7
        return dayofWeekNames[dow]


tests = [
    (31, 8, 2019, "Saturday"),
    (18, 7, 1999, "Sunday"),
    (15, 8, 1993, "Sunday")
]

for test in tests:
    result = Solution().dayOfTheWeek(test[0], test[1], test[2])
    if result == test[3]:
        print("PASS")
    else:
        print("FAIL - " + result)