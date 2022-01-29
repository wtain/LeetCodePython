"""
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.



Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [1,12], arr = [12,1]
Output: true
Example 4:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr doesn't have value 9 and it can never be converted to target.
Example 5:

Input: target = [1,1,1,1,1], arr = [1,1,1,1,1]
Output: true


Constraints:

target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 172 ms, faster than 5.41% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
# Memory Usage: 14.6 MB, less than 31.41% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         return Counter(target) == Counter(arr)


# Runtime: 72 ms, faster than 91.70% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
# Memory Usage: 14.4 MB, less than 62.26% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         return sorted(target) == sorted(arr)


# Runtime: 144 ms, faster than 6.95% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
# Memory Usage: 14.6 MB, less than 31.41% of Python3 online submissions for Make Two Arrays Equal by Reversing Sub-arrays.
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return all(a == b for a, b in zip(sorted(target), sorted(arr)))


tests = [
    [[7], [7], True],
    [[1,12], [12,1], True],
    [[3,7,9], [3,7,11], False],
    [[1,1,1,1,1], [1,1,1,1,1], True]
]

run_functional_tests(Solution().canBeEqual, tests)