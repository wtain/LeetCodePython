"""
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6


Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
from bisect import bisect_left, bisect_right
from typing import List


# Runtime: 88 ms, faster than 77.16% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
# Memory Usage: 15.5 MB, less than 35.50% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        n1 = n // 4
        n2 = n // 2
        n3 = (3 * n) // 4
        a0 = arr[0]
        a1 = arr[n1]
        a2 = arr[n2]
        a3 = arr[n3]
        a4 = arr[n-1]
        n4 = n // 4

        def find_frequency(i: int) -> int:
            nonlocal arr, n
            i1 = bisect_left(arr, arr[i], 0, n)
            i2 = bisect_right(arr, arr[i], 0, n)
            return i2 - i1

        f0 = find_frequency(0)
        if f0 > n4:
            return a0
        f1 = find_frequency(n1)
        if f1 > n4:
            return a1
        f2 = find_frequency(n2)
        if f2 > n4:
            return a2

        return a3
        #f3 = find_frequency(n3)
        #if f3 > n4:
        #    return a3

        #print(f0, f1, f2, f3)

        #return 0


tests = [
    ([1,2,2,6,6,6,6,7,10], 6),
    ([1], 1)
]

for test in tests:
    result = Solution().findSpecialInteger(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
