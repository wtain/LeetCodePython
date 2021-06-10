"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).



Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].


Constraints:

0 <= low <= high <= 10^9
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 40 ms, faster than 6.88% of Python3 online submissions for Count Odd Numbers in an Interval Range.
# Memory Usage: 14.2 MB, less than 69.40% of Python3 online submissions for Count Odd Numbers in an Interval Range.
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         result = (high - low) // 2
#         if low % 2 or high % 2:
#             result += 1
#         return result


# Runtime: 36 ms, faster than 6.88% of Python3 online submissions for Count Odd Numbers in an Interval Range.
# Memory Usage: 14.3 MB, less than 39.68% of Python3 online submissions for Count Odd Numbers in an Interval Range.
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + max(low % 2, high % 2)


tests = [
    [21, 22, 1],
    [3, 7, 3],
    [8, 10, 1]
]

run_functional_tests(Solution().countOdds, tests)