"""
https://leetcode.com/problems/number-of-days-between-two-dates/

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15


Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""


# Runtime: 36 ms, faster than 34.82% of Python3 online submissions for Number of Days Between Two Dates.
# Memory Usage: 14.4 MB, less than 14.21% of Python3 online submissions for Number of Days Between Two Dates.
# class Solution:
#     def daysBetweenDates(self, date1: str, date2: str) -> int:
#
#         def parse_date(date: str) -> (int, int, int):
#             return int(date[:4]), int(date[5:7]), int(date[8:])
#
#         def is_leap(y: int) -> bool:
#             return y % 400 == 0 or y % 4 == 0 and y % 100 != 0
#
#         def days_in_month(m: int, y: int) -> int:
#             if m in [1, 3, 5, 7, 8, 10, 12]:
#                 return 31
#             elif m == 2:
#                 return 29 if is_leap(y) else 28
#             else:
#                 return 30
#
#         def days_in_year(y: int) -> int:
#             return 366 if is_leap(y) else 365
#
#         def num_epoch_days(date: str) -> int:
#             y1, m1, d1 = parse_date(date)
#             result = 0
#             for y in range(1900, y1):
#                 result += days_in_year(y)
#             for m in range(1, m1):
#                 result += days_in_month(m, y1)
#             result += d1 - 1
#             return result
#
#         return abs(num_epoch_days(date2) - num_epoch_days(date1))


# Runtime: 36 ms, faster than 34.82% of Python3 online submissions for Number of Days Between Two Dates.
# Memory Usage: 14.5 MB, less than 14.21% of Python3 online submissions for Number of Days Between Two Dates.
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def parse_date(date: str) -> (int, int, int):
            return int(date[:4]), int(date[5:7]), int(date[8:])

        def is_leap(y: int) -> bool:
            return y % 400 == 0 or y % 4 == 0 and y % 100 != 0

        def days_in_month(m: int, y: int) -> int:
            if m in [1, 3, 5, 7, 8, 10, 12]:
                return 31
            elif m == 2:
                return 29 if is_leap(y) else 28
            else:
                return 30

        def days_in_year(y: int) -> int:
            return 366 if is_leap(y) else 365

        def num_epoch_days(date: str) -> int:
            y1, m1, d1 = parse_date(date)
            return sum([days_in_year(y) for y in range(1900, y1)]) + \
                   sum([days_in_month(m, y1) for m in range(1, m1)]) + \
                   d1 - 1

        return abs(num_epoch_days(date2) - num_epoch_days(date1))


tests = [
    ("2019-06-29", "2019-06-30", 1),
    ("2020-01-15", "2019-12-31", 15)
]

for test in tests:
    result = Solution().daysBetweenDates(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
