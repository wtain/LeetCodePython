"""
https://leetcode.com/problems/array-of-doubled-pairs/

Given an array of integers arr of even length, return true if and only if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.



Example 1:

Input: arr = [3,1,3,6]
Output: false
Example 2:

Input: arr = [2,1,2,6]
Output: false
Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: arr = [1,2,4,16,8,4]
Output: false


Constraints:

0 <= arr.length <= 3 * 104
arr.length is even.
-105 <= arr[i] <= 105
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 572 ms, faster than 87.38% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.5 MB, less than 63.12% of Python3 online submissions for Array of Doubled Pairs.
# Runtime: 576 ms, faster than 84.05% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.7 MB, less than 38.21% of Python3 online submissions for Array of Doubled Pairs.
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        arr2 = sorted(c.keys(), key=lambda x: abs(x))
        # arr2 = list(c.keys())
        m = len(arr2)
        total_cnt = len(arr) - c[0]
        for x in arr2:
            if c[x]:
                if x:
                    other = 2*x
                    cm = min(c[x], c[other])
                    c[x] -= cm
                    c[other] -= cm
                    total_cnt -= 2 * cm
        return total_cnt == 0

# Runtime: 764 ms, faster than 23.59% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.8 MB, less than 19.60% of Python3 online submissions for Array of Doubled Pairs.
# class Solution:
#     def canReorderDoubled(self, arr: List[int]) -> bool:
#         c = Counter(arr)
#         for x in sorted(arr, key=abs):
#             if not c[x]:
#                 continue
#             if not c[2*x]:
#                 return False
#             c[2*x] -= 1
#             c[x] -= 1
#         return True


tests = [
    [[2,1,1,4,8,8], False],
    [[-6,2,-6,4,-3,8,3,2,-2,6,1,-3,-4,-4,-8,4], True],
    [[-5,-3], False],
    [[-2,-6,-3,4,-4,2], True],
    [[-2,-2,1,-2,-1,2], False],
    [[0,0], True],
    [[2,1,2,1,1,1,2,2], True],

    [[3,1,3,6], False],
    [[2,1,2,6], False],
    [[4,-2,2,-4], True],
    [[1,2,4,16,8,4], False]
]

# run_functional_tests(Solution().canReorderDoubled, tests, run_tests=[2, 5, 8])
run_functional_tests(Solution().canReorderDoubled, tests)

# run_functional_tests(Solution().canReorderDoubled, tests, run_tests=[1])