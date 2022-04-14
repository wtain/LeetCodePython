"""
https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

0 <= i <= nums.length - 2,
nums[i] == key and,
nums[i + 1] == target.
Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.



Example 1:

Input: nums = [1,100,200,1,100], key = 1
Output: 100
Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
No other integers follow an occurrence of key, so we return 100.
Example 2:

Input: nums = [2,2,2,2,3], key = 2
Output: 2
Explanation: For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key.
For target = 3, there is only one occurrence at index 4 which follows an occurrence of key.
target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.


Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
The test cases will be generated such that the answer is unique.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 118 ms, faster than 54.96% of Python3 online submissions for Most Frequent Number Following Key In an Array.
# Memory Usage: 14.1 MB, less than 92.36% of Python3 online submissions for Most Frequent Number Following Key In an Array.
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = defaultdict(int)
        n = len(nums)
        max_cnt, target = 0, 0
        for i in range(n-1):
            if nums[i] == key:
                d[nums[i+1]] += 1
                if d[nums[i+1]] >= max_cnt:
                    max_cnt = d[nums[i+1]]
                    target = nums[i+1]

        return target


tests = [
    [[1,100,200,1,100], 1, 100],
    [[2,2,2,2,3], 2, 2]
]

run_functional_tests(Solution().mostFrequent, tests)
