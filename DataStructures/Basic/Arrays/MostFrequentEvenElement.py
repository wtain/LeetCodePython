"""
https://leetcode.com/problems/most-frequent-even-element/

Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.



Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.


Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 777 ms
# Beats
# 38.19%
# Memory
# 14.3 MB
# Beats
# 58.54%
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(filter(lambda x: x % 2 == 0, nums))
        if len(counter.keys()) == 0:
            return -1
        return - max([cnt, -v] for v, cnt in counter.items())[1]


tests = [
    [[0,1,2,2,4,4,1], 2],
    [[4,4,4,9,2,4], 4],
    [[29,47,21,41,13,37,25,7], -1]
]

run_functional_tests(Solution().mostFrequentEven, tests)
