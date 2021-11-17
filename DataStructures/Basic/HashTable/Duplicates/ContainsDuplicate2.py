"""
https://leetcode.com/problems/contains-duplicate-ii/
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
from queue import Queue
from typing import List, Dict

# NO Queues
from Common.ObjectTestingUtils import run_functional_tests

"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nearby: Dict[int, int] = {}
        window: Queues[int] = Queues()
        for i, num in enumerate(nums):
            if num in nearby:
                return True
            if len(nearby) == k:
                num1 = window.get()
                if nearby[num1] == i-k:
                    del nearby[num1]
            nearby[num] = i
            window.put(num)
        return False
"""

"""
Runtime: 216 ms, faster than 5.51% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 21.3 MB, less than 80.09% of Python3 online submissions for Contains Duplicate II.
"""
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nearby: Dict[int, int] = {}
        window: List[int] = []
        if k == 0:
            return False
        for i, num in enumerate(nums):
            if num in nearby:
                return True
            if len(nearby) == k:
                num1 = window[0]
                del window[0]
                if nearby[num1] == i-k:
                    del nearby[num1]
            nearby[num] = i
            window.append(num)
        return False
"""

"""
Runtime: 116 ms, faster than 37.79% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 21.3 MB, less than 77.88% of Python3 online submissions for Contains Duplicate II.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nearby: Dict[int, int] = {}
        if k == 0:
            return False
        window: List[int] = [-1] * k
        w = r = 0
        for i, num in enumerate(nums):
            if num in nearby:
                return True
            if len(nearby) == k:
                num1 = window[r]
                r += 1
                r %= k
                if nearby[num1] == i-k:
                    del nearby[num1]
            nearby[num] = i
            window[w] = num
            w += 1
            w %= k
        return False


tests = [
    [[1,2,1], 0, False],
    [[1,2,3,1], 3, True],
    [[1,0,1,1], 1, True],
    [[1,2,3,1,2,3], 2, False]
]

run_functional_tests(Solution().containsNearbyDuplicate, tests)
