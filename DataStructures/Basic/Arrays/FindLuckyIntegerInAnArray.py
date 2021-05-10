"""
https://leetcode.com/problems/find-lucky-integer-in-an-array/

Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.



Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
Example 4:

Input: arr = [5]
Output: -1
Example 5:

Input: arr = [7,7,7,7,7,7,7]
Output: 7


Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 87.46% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 14.4 MB, less than 12.04% of Python3 online submissions for Find Lucky Integer in an Array.
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = -1
        c = Counter(arr)
        for x in arr:
            if x == c[x] and x > result:
                result = x
        return result


tests = [
    [[2,2,3,4], 2],
    [[1,2,2,3,3,3], 3],
    [[2,2,2,3,3], -1],
    [[5], -1],
    [[7,7,7,7,7,7,7], 7]
]

run_functional_tests(Solution().findLucky, tests)