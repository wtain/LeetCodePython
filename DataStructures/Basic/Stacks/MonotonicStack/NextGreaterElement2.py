"""
https://leetcode.com/problems/next-greater-element-ii/

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.



Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]


Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 228 ms, faster than 60.98% of Python3 online submissions for Next Greater Element II.
# Memory Usage: 15.7 MB, less than 87.95% of Python3 online submissions for Next Greater Element II.
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st, result = [], [-1] * n
        for i1 in range(2*n):
            i = i1 % n
            while st and nums[st[-1]] < nums[i]:
                result[st[-1]] = nums[i]
                st.pop()
            st.append(i)
        return result


tests = [
    [[1,2,1], [2,-1,2]],
    [[1,2,3,4,3], [2,3,4,-1,4]]
]

run_functional_tests(Solution().nextGreaterElements, tests)
