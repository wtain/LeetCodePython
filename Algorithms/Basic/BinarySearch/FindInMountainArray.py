"""
https://leetcode.com/problems/find-in-mountain-array/description/?envType=daily-question&envId=2023-10-12

(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.


Constraints:

3 <= mountain_arr.length() <= 104
0 <= target <= 109
0 <= mountain_arr.get(index) <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.calls = 0

    def get(self, index: int) -> int:
        self.calls += 1
        if self.calls > 100:
            raise RuntimeError('Too many calls')
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


# Runtime
# Details
# 39ms
# Beats 50.85%of users with Python3
# Memory
# Details
# 17.17MB
# Beats 60.00%of users with Python3
# https://leetcode.com/problems/find-in-mountain-array/editorial/?envType=daily-question&envId=2023-10-12
# class Solution:
#     def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
#         length = mountain_arr.length()
#         low, high = 1, length - 2
#         while low != high:
#             test_index = (low + high) // 2
#             if mountain_arr.get(test_index) < mountain_arr.get(test_index+1):
#                 low = test_index + 1
#             else:
#                 high = test_index
#         peak_index = low
#
#         low, high = 0, peak_index
#         while low != high:
#             test_index = (low + high) // 2
#             if mountain_arr.get(test_index) < target:
#                 low = test_index + 1
#             else:
#                 high = test_index
#         if mountain_arr.get(low) == target:
#             return low
#
#         low, high = peak_index+1, length - 1
#         while low != high:
#             test_index = (low + high) // 2
#             if mountain_arr.get(test_index) > target:
#                 low = test_index + 1
#             else:
#                 high = test_index
#         if mountain_arr.get(low) == target:
#             return low
#
#         return -1



# Runtime
# Details
# 37ms
# Beats 70.08%of users with Python3
# Memory
# Details
# 17.07MB
# Beats 90.39%of users with Python3
# https://leetcode.com/problems/find-in-mountain-array/editorial/?envType=daily-question&envId=2023-10-12
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        cache = {}
        low, high = 1, length - 2
        while low != high:
            test_index = (low + high) // 2

            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
                cache[test_index] = curr

            if test_index+1 in cache:
                next = cache[test_index+1]
            else:
                next = mountain_arr.get(test_index+1)
                cache[test_index+1] = next

            if curr < next:
                if curr == target:
                    return test_index
                if next == target:
                    return test_index + 1
                low = test_index + 1
            else:
                high = test_index
        peak_index = low

        low, high = 0, peak_index
        while low <= high:
            test_index = (low + high) // 2

            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)

            if curr == target:
                return test_index
            elif curr < target:
                low = test_index + 1
            else:
                high = test_index - 1

        low, high = peak_index+1, length - 1
        while low <= high:
            test_index = (low + high) // 2

            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)

            if curr == target:
                return test_index
            elif curr > target:
                low = test_index + 1
            else:
                high = test_index - 1

        return -1


tests = [
    [[1,2,3,4,5,3,1], 3, 2],
    [[0,1,2,4,2,1], 3, -1],
]


run_functional_tests(Solution().findInMountainArray, list(map(lambda test: [test[1], MountainArray(test[0]), test[2]], tests)))

