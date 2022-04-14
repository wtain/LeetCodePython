"""
https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.



Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.
Example 2:

Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.


Constraints:

current and correct are in the format "HH:MM"
current <= correct
"""
from Common.ObjectTestingUtils import run_functional_tests

# Runtime: 55 ms, faster than 50.00% of Python3 online submissions for Minimum Number of Operations to Convert Time.
# Memory Usage: 13.8 MB, less than 66.67% of Python3 online submissions for Minimum Number of Operations to Convert Time.
class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        def parse_time(t: str) -> (int, int):
            return int(t[:2]), int(t[3:])

        def convert_to_minutes(h: int, m: int) -> int:
            return h * 60 + m

        h1, m1 = parse_time(current)
        h2, m2 = parse_time(correct)

        t1, t2 = convert_to_minutes(h1, m1), convert_to_minutes(h2, m2)
        diff = t2 - t1
        cnt = diff // 60
        diff %= 60
        cnt += diff // 15
        diff %= 15
        cnt += diff // 5
        diff %= 5
        cnt += diff

        return cnt


tests = [
    ["02:30", "04:35", 3],
    ["11:00", "11:01", 1]
]

run_functional_tests(Solution().convertTime, tests)
