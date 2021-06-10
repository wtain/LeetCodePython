"""
https://leetcode.com/problems/three-consecutive-odds/

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.


Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 80 ms, faster than 5.15% of Python3 online submissions for Three Consecutive Odds.
# Memory Usage: 14.1 MB, less than 99.21% of Python3 online submissions for Three Consecutive Odds.
# class Solution:
#     def threeConsecutiveOdds(self, arr: List[int]) -> bool:
#         n = len(arr)
#         for i in range(1, n-1):
#             if arr[i-1] % 2 == 0:
#                 continue
#             if arr[i] % 2 == 0:
#                 continue
#             if arr[i + 1] % 2 == 0:
#                 continue
#             return True
#         return False


# Runtime: 48 ms, faster than 47.95% of Python3 online submissions for Three Consecutive Odds.
# Memory Usage: 14.4 MB, less than 53.10% of Python3 online submissions for Three Consecutive Odds.
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any((a1 % 2)*(a2 % 2)*(a3 % 2) > 0 for a1, a2, a3 in zip(arr, arr[1:], arr[2:]))


tests = [
    [[2,6,4,1], False],
    [[1,2,34,3,4,5,7,23,12], True]
]

run_functional_tests(Solution().threeConsecutiveOdds, tests)