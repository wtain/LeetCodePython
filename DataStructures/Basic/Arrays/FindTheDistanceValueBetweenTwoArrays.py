"""
https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.



Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1


Constraints:

1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 64 ms, faster than 99.48% of Python3 online submissions for Find the Distance Value Between Two Arrays.
# Memory Usage: 14.4 MB, less than 39.48% of Python3 online submissions for Find the Distance Value Between Two Arrays.
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2)
        cnt = 0
        for x in arr1:
            i = bisect.bisect_left(arr2, x)
            if i < len(arr2) and abs(arr2[i]-x) <= d:
                continue
            if i-1 >= 0 and abs(arr2[i-1]-x) <= d:
                continue
            # l, r = x - d, x + d
            # i1 = bisect.bisect_left(arr2, l)
            # if i1 < len(arr2) and arr2[i1] < l:
            #     continue
            # i2 = bisect.bisect_left(arr2, r)
            # if i2 < len(arr2) and arr2[i2] > r:
            #     continue
            cnt += 1

        return cnt


tests = [
    [[-3,2,-5,7,1], [4], 84, 0],
    [[4,5,8], [10,9,1,8], 2, 2],
    [[1,4,2,3], [-4,-3,6,10,20,30], 3, 2],
    [[2,1,100,3], [-5,-2,10,-3,7], 6, 1]
]

run_functional_tests(Solution().findTheDistanceValue, tests)