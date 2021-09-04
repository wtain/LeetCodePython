"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/
https://leetcode.com/problems/count-binary-substrings/

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 284 ms, faster than 9.45% of Python3 online submissions for Count Binary Substrings.
# Memory Usage: 14.5 MB, less than 93.13% of Python3 online submissions for Count Binary Substrings.
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         if not s:
#             return 0
#         cnt = 0
#         n = len(s)
#         i1 = 0
#         while i1 < n:
#             s0 = s[i1]
#             i2 = i1
#             while i2 < n and s[i2] == s[i1]:
#                 i2 += 1
#             c1 = i2 - i1
#             c2 = 0
#             j = i2
#             while i2 < n and s[i2] != s[i1] and c2 < c1:
#                 i2 += 1
#                 c2 += 1
#             cnt += i2 - j
#             if i2 == n:
#                 break
#             i1 = j
#         return cnt


# Runtime: 156 ms, faster than 80.81% of Python3 online submissions for Count Binary Substrings.
# Memory Usage: 14.4 MB, less than 99.61% of Python3 online submissions for Count Binary Substrings.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result, prev, curr = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        return result + min(prev, curr)


tests = [
    ["", 0],

    ["00110011", 6],
    ["10101", 4]
]

run_functional_tests(Solution().countBinarySubstrings, tests)