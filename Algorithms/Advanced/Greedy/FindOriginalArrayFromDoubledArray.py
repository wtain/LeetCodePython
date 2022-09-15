"""
https://leetcode.com/problems/find-original-array-from-doubled-array/

An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.



Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.


Constraints:

1 <= changed.length <= 105
0 <= changed[i] <= 105


If changed is a doubled array, you should be able to delete elements and their doubled values until the array is empty.


Which element is guaranteed to not be a doubled value? It is the smallest element.


After removing the smallest element and its double from changed, is there another number that is guaranteed to not be a doubled value?
"""
from collections import defaultdict
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         deleted, to_delete = defaultdict(int), defaultdict(int)
#         for v in sorted(changed):
#             if to_delete[v] > 0:
#                 to_delete[v] -= 1
#                 deleted[v // 2] += 1
#             else:
#                 to_delete[2*v] += 1
#         if any(v > 0 for k, v in to_delete.items()):
#             return []
#         return reduce(lambda res, k: res + [k[0]] * k[1], deleted.items(), [])


# Runtime: 5836 ms, faster than 5.13% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 38 MB, less than 5.12% of Python3 online submissions for Find Original Array From Doubled Array.
# class Solution:
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         deleted, to_delete = defaultdict(int), defaultdict(int)
#         for v in sorted(changed):
#             if to_delete[v] > 0:
#                 to_delete[v] -= 1
#                 if to_delete[v] == 0:
#                     del to_delete[v]
#                 deleted[v // 2] += 1
#             else:
#                 to_delete[2*v] += 1
#         if any(v > 0 for k, v in to_delete.items()):
#             return []
#         return reduce(lambda res, k: res + [k[0]] * k[1], deleted.items(), [])


# Runtime: 3325 ms, faster than 12.75% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 39.6 MB, less than 5.12% of Python3 online submissions for Find Original Array From Doubled Array.
# class Solution:
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
#         result, to_delete = [], defaultdict(int)
#         for v in sorted(changed):
#             if to_delete[v] > 0:
#                 to_delete[v] -= 1
#                 if to_delete[v] == 0:
#                     del to_delete[v]
#                 result.append(v // 2)
#             else:
#                 to_delete[2*v] += 1
#         if any(v > 0 for k, v in to_delete.items()):
#             return []
#         return result


# Runtime: 3670 ms, faster than 7.33% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 34.3 MB, less than 14.35% of Python3 online submissions for Find Original Array From Doubled Array.
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        result, to_delete = [], defaultdict(int)
        for v in sorted(changed):
            if v in to_delete:
                to_delete[v] -= 1
                if to_delete[v] == 0:
                    del to_delete[v]
                result.append(v // 2)
            else:
                to_delete[2*v] += 1
        if len(to_delete) > 0:
            return []
        return result


tests = [
    [[1,3,4,2,6,8], [1,3,4]],
    [[6,3,0,1], []],
    [[1], []]
]

run_functional_tests(Solution().findOriginalArray, tests)
