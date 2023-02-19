"""
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/description/

Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.



Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361


Constraints:

1 <= arr.length <= 104
1 <= arr[i], target <= 105
"""
import bisect
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 103 ms
# Beats
# 79.22%
# Memory
# 15.2 MB
# Beats
# 79.82%
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        s = sum(arr)
        mindiff = float('inf')
        result = float('inf')
        n = len(arr)
        vmin, vmax = arr[0], arr[-1]
        ps = [0] + list(accumulate(arr))
        l, r = 0, vmax
        while l <= r:
            m = l + (r - l) // 2
            j = bisect.bisect_right(arr, m)
            s1 = ps[j] + (n-j) * m
            diff = abs(s1-target)
            # print(l, r, m, j, s1)
            if diff < mindiff or diff == mindiff and m < result:
                mindiff = diff
                result = m
            if s1 < target:
                l = m+1
            elif s1 > target:
                r = m-1
            else:
                return m
        return result


tests = [
    [[1,1,2], 10, 2],
    [[1547,83230,57084,93444,70879], 71237, 17422],
    [[4,9,3], 10, 3],
    [[2,3,5], 10, 5],
    [[60864,25176,27249,21296,20204], 56803, 11361],
]

run_functional_tests(Solution().findBestValue, tests)
