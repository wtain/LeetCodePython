"""
https://leetcode.com/problems/decompress-run-length-encoded-list/

We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.



Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
Example 2:

Input: nums = [1,1,2,3]
Output: [1,3,3]


Constraints:

2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
"""
from typing import List


# Runtime: 60 ms, faster than 92.94% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 14.8 MB, less than 29.67% of Python3 online submissions for Decompress Run-Length Encoded List.
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        n2 = n // 2
        for i in range(n2):
            f = nums[2*i]
            v = nums[2*i+1]
            result.extend([v] * f)
        return result


tests = [
    ([1,2,3,4], [2,4,4,4]),
    ([1,1,2,3], [1,3,3])
]

for test in tests:
    result = Solution().decompressRLElist(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))