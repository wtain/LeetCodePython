"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12


Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""
import heapq
from typing import List


# Runtime: 48 ms, faster than 84.24% of Python3 online submissions for Maximum Product of Two Elements in an Array.
# Memory Usage: 14.4 MB, less than 13.40% of Python3 online submissions for Maximum Product of Two Elements in an Array.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h = []
        for a in nums:
            heapq.heappush(h, a)
            if len(h) > 2:
                heapq.heappop(h)
        return (h[0]-1) * (h[1]-1)



tests = [
    ([3,4,5,2], 12),
    ([1,5,4,5], 16),
    ([3,7], 12)
]

for test in tests:
    result = Solution().maxProduct(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))