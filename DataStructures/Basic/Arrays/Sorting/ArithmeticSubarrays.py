"""
https://leetcode.com/problems/arithmetic-subarrays/description/?envType=daily-question&envId=2023-11-23

A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.



Example 1:

Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
Example 2:

Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]


Constraints:

n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-105 <= nums[i] <= 105
"""
from typing import List

from Common.Constants import true, false
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 162
# ms
# Beats
# 76.39%
# of users with Python3
# Memory
# 16.67
# MB
# Beats
# 14.03%
# of users with Python3
# https://leetcode.com/problems/arithmetic-subarrays/editorial/?envType=daily-question&envId=2023-11-23
# class Solution:
#     def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
#
#         def check(arr):
#             arr.sort()
#             diff = arr[1] - arr[0]
#             for i in range(2, len(arr)):
#                 if arr[i] - arr[i-1] != diff:
#                     return False
#             return True
#
#         result = []
#         for i in range(len(l)):
#             arr = nums[l[i]:r[i]+1]
#             result.append(check(arr))
#
#         return result


# Runtime
# 157
# ms
# Beats
# 90.20%
# of users with Python3
# Memory
# 16.40
# MB
# Beats
# 93.32%
# of users with Python3
# https://leetcode.com/problems/arithmetic-subarrays/editorial/?envType=daily-question&envId=2023-11-23
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            min_element, max_element = min(arr), max(arr)
            if (max_element - min_element) % (len(arr)-1) != 0:
                return False
            diff = (max_element - min_element) / (len(arr)-1)
            arr_set = set(arr)
            curr = min_element + diff
            while curr < max_element:
                if curr not in arr_set:
                    return False
                curr += diff
            return True

        result = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            result.append(check(arr))
        return result


tests = [
    [[4,6,5,9,3,7], [0,0,2], [2,3,5], [true,false,true]],
    [[-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10], [false,true,false,false,true,true]],
]

run_functional_tests(Solution().checkArithmeticSubarrays, tests)
