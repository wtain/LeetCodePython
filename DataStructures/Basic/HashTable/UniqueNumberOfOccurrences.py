"""
https://leetcode.com/problems/unique-number-of-occurrences/description/

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 76 ms
# Beats
# 30.27%
# Memory
# 14.1 MB
# Beats
# 5.18%
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return len(cnt.keys()) == len(set(cnt.values()))


tests = [
    [[1,2,2,1,1,3], True],
    [[1,2], False],
    [[-3,0,1,-3,1,1,1,-3,10,0], True]
]

run_functional_tests(Solution().uniqueOccurrences, tests)
