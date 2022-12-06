"""
https://leetcode.com/problems/number-of-valid-clock-times/

You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.



Example 1:

Input: time = "?5:00"
Output: 2
Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
Example 2:

Input: time = "0?:0?"
Output: 100
Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
Example 3:

Input: time = "??:??"
Output: 1440
Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.


Constraints:

time is a valid string of length 5 in the format "hh:mm".
"00" <= hh <= "23"
"00" <= mm <= "59"
Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 63 ms
# Beats
# 30.46%
# Memory
# 14 MB
# Beats
# 26.17%
class Solution:
    def countTime(self, time: str) -> int:
        h, m = time[:2], time[3:]
        valid_hours, valid_minutes = 1, 1
        if h == '??':
            valid_hours = 24
        elif h[0] == '?':
            if int(h[1]) <= 3:
                valid_hours = 3
            else:
                valid_hours = 2
        elif h[1] == '?':
            if int(h[0]) < 2:
                valid_hours = 10
            else:
                valid_hours = 4
        if m == '??':
            valid_minutes = 60
        elif m[0] == '?':
            valid_minutes = 6
        elif m[1] == '?':
            valid_minutes = 10
        return valid_hours * valid_minutes


tests = [
    ["?5:00", 2],
    ["0?:0?", 100],
    ["??:??", 1440]
]

run_functional_tests(Solution().countTime, tests)
