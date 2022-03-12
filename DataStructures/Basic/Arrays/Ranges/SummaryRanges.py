"""
https://leetcode.com/problems/summary-ranges/
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.

Runtime: 36 ms, faster than 32.80% of Python3 online submissions for Summary Ranges.
Memory Usage: 14 MB, less than 75.44% of Python3 online submissions for Summary Ranges.

"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 29 ms, faster than 87.42% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.9 MB, less than 88.25% of Python3 online submissions for Summary Ranges.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result: List[str] = []
        n = len(nums)
        start = None

        def appendRange(start: int, j: int):
            if start == nums[j]:
                result.append(str(nums[j]))
            else:
                result.append(str(start) + "->" + str(nums[j]))

        for i in range(n):
            if start is None:
                start = nums[i]
            elif nums[i] != nums[i-1] + 1:
                appendRange(start, i-1)
                start = nums[i]
        if start is not None:
            appendRange(start, n-1)
        return result


tests = [
    [[0,1,2,4,5,7], ["0->2","4->5","7"]],
    [[0,2,3,4,6,8,9], ["0","2->4","6","8->9"]],
    [[], []],
    [[-1], ["-1"]],
    [[0], ["0"]]
]

run_functional_tests(Solution().summaryRanges, tests)
