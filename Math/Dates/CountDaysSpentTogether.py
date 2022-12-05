"""
https://leetcode.com/problems/count-days-spent-together/

Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].



Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.


Constraints:

All dates are provided in the format "MM-DD".
Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
The given dates are valid dates of a non-leap year.
"""
import numpy

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 107 ms
# Beats
# 5.63%
# Memory
# 31.5 MB
# Beats
# 16.51%
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_before_month = [0] + list(numpy.cumsum(days_in_month))

        def day_of_year(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])
            return days_before_month[month-1] + day-1

        a1, a2 = day_of_year(arriveAlice), day_of_year(leaveAlice)
        b1, b2 = day_of_year(arriveBob), day_of_year(leaveBob)

        if a2 < b1 or b2 < a1:
            return 0

        return min(a2, b2) - max(a1, b1)+1


tests = [
    ["08-15", "08-18", "08-16", "08-19", 3],
    ["10-01", "10-31", "11-01", "12-31", 0]
]

run_functional_tests(Solution().countDaysTogether, tests)
