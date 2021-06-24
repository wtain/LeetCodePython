"""
https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.



Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"


Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 61.28% of Python3 online submissions for Latest Time by Replacing Hidden Digits.
# Memory Usage: 14.1 MB, less than 75.43% of Python3 online submissions for Latest Time by Replacing Hidden Digits.
class Solution:
    def maximumTime(self, time: str) -> str:
        h, m = time.split(':', 2)

        def build_part(part: str, max_v1: str, max_v2: str) -> str:
            result = ""
            if part[0] == '?':
                if part[1] == '?' or part[1] <= max_v2:
                    result += max_v1
                else:
                    result += chr(ord(max_v1)-1)
            else:
                result += part[0]
            if part[1] == '?':
                if result[-1] == max_v1:
                    result += max_v2
                else:
                    result += "9"
            else:
                result += part[1]
            return result

        return build_part(h, '2', '3') + ":" + build_part(m, '5', '9')


tests = [
    ["01:?9", "01:59"],

    ["?4:03", "14:03"],

    ["2?:?0", "23:50"],
    ["0?:3?", "09:39"],
    ["1?:22", "19:22"]
]

run_functional_tests(Solution().maximumTime, tests)