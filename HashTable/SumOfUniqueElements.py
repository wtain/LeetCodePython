"""
https://leetcode.com/problems/sum-of-unique-elements/

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.



Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List, Dict


# Runtime: 36 ms, faster than 68.56% of Python3 online submissions for Sum of Unique Elements.
# Memory Usage: 14.2 MB, less than 47.78% of Python3 online submissions for Sum of Unique Elements.
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts: Dict[int, int] = {}
        result = 0
        for a in nums:
            cnt = counts.get(a, 0)
            if cnt == 0:
                result += a
            elif cnt == 1:
                result -= a
            counts[a] = cnt + 1

        return result


tests = [
    ([1,2,3,2], 4),
    ([1,1,1,1,1], 0),
    ([1,2,3,4,5], 15)
]

for test in tests:
    result = Solution().sumOfUnique(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))