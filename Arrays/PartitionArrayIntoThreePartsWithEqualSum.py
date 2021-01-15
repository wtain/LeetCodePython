"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])



Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104
"""
from typing import List


# Runtime: 304 ms, faster than 71.41% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
# Memory Usage: 21.1 MB, less than 19.43% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        S = sum(arr)
        if S % 3 != 0:
            return False
        si = S // 3

        s1 = arr[0]
        i = 1
        while i < n and s1 != si:
            s1 += arr[i]
            i += 1
        if i > n-2:
            return False

        j = n-2
        s3 = arr[n-1]
        while j > i and s3 != si:
            s3 += arr[j]
            j -= 1
        return s3 == si


tests = [
    ([1,-1,1,-1], False),

    ([18,12,-18,18,-19,-1,10,10], True),

    ([14,6,-10,2,18,-7,-4,11], False),

    ([0,2,1,-6,6,-7,9,1,2,0,1], True),
    ([0,2,1,-6,6,7,9,-1,2,0,1], False),
    ([3,3,6,5,-2,2,5,1,-9,4], True)
]

for test in tests:
    result = Solution().canThreePartsEqualSum(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))