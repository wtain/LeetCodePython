"""
https://leetcode.com/problems/intersection-of-multiple-arrays/

Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.


Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation:
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation:
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].


Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# WRONG
# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         nums = [sorted(arr) for arr in nums]
#         n = len(nums)
#         counters = [0] * n
#         result = []
#         while all(counters[i] < len(nums[i]) for i in range(n)):
#             mv = max(nums[i][counters[i]] for i in range(n))
#             end_reached = False
#             for i in range(n):
#                 while counters[i] < len(nums[i]) and nums[i][counters[i]] < mv:
#                     counters[i] += 1
#                 if counters[i] == len(nums[i]):
#                     end_reached = True
#                     break
#             if end_reached:
#                 break
#             result.append(mv)
#             for i in range(n):
#                 counters[i] += 1
#         return result


# Runtime: 105 ms, faster than 33.73% of Python3 online submissions for Intersection of Multiple Arrays.
# Memory Usage: 14.3 MB, less than 31.71% of Python3 online submissions for Intersection of Multiple Arrays.
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums = [sorted(arr) for arr in nums]
        n = len(nums)
        counters = [0] * n
        result = []
        while all(counters[i] < len(nums[i]) for i in range(n)):
            mv = max(nums[i][counters[i]] for i in range(n))
            end_reached = False
            not_found = False
            for i in range(n):
                while counters[i] < len(nums[i]) and nums[i][counters[i]] < mv:
                    counters[i] += 1
                if counters[i] == len(nums[i]):
                    end_reached = True
                    break
                if nums[i][counters[i]] > mv:
                    not_found = True
            if end_reached:
                break
            if not_found:
                continue
            result.append(mv)
            for i in range(n):
                counters[i] += 1
        return result


tests = [
    [[[25,44,47,42,43,10],[40,10,8,30,5,23],[36,10]], [10]],
    [[[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], [3,4]],
    [[[1,2,3],[4,5,6]], []]
]

run_functional_tests(Solution().intersection, tests)
