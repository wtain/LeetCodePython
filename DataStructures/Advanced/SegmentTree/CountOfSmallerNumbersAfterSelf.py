"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3792/
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from collections import Counter, defaultdict
from typing import List

from sortedcontainers import SortedSet, SortedList

from Common.ObjectTestingUtils import run_functional_tests

# Runtime: 2744 ms, faster than 75.07% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 43.4 MB, less than 16.60% of Python3 online submissions for Count of Smaller Numbers After Self.
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         s = SortedSet()
#         result = [0] * n
#         c = defaultdict(int)
#         for i in range(n-1, -1, -1):
#             result[i] = s.bisect_left((nums[i], -c[nums[i]]))
#             c[nums[i]] += 1
#             s.add((nums[i], -c[nums[i]]))
#         return result

# WRONG
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         s = SortedSet()
#         result = [0] * n
#         for i in range(n-1, -1, -1):
#             result[i] = s.bisect_left(nums[i])
#             s.add(nums[i])
#         return result

# Runtime: 2228 ms, faster than 89.08% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 34.1 MB, less than 58.33% of Python3 online submissions for Count of Smaller Numbers After Self.
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/1297647/Python-SortedList-solution-explained
class Solution:
    def countSmaller(self, nums):
        SList, ans = SortedList(), []
        for num in reversed(nums):
            ind = SList.bisect_left(num)
            ans.append(ind)
            SList.add(num)

        return ans[::-1]


tests = [
    [
        [5183,5183,5183],
        [0,0,0]
    ],
    [
        [90,23,66,5,38,7,35,23,52,22],
        [9,3,7,0,4,0,2,1,1,0]
    ],
    [
        [100,33,67,90,23,66,5,38,7,35,23,52,22],
        [12,5,9,9,3,7,0,4,0,2,1,1,0]
    ],
    [
        [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22],
        [5,12,5,12,5,9,9,3,7,0,4,0,2,1,1,0]
    ],
    [
        [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41],
        [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
    #   [9,24,9,32,11,19,25,8,18,2,12,2,9,6,11,5,16,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
    ],

    [[5,2,6,1], [2,1,1,0]],
    [[-1], [0]],
    [[-1,-1], [0,0]]
]

run_functional_tests(Solution().countSmaller, tests)