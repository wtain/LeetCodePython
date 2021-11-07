"""
https://leetcode.com/problems/maximum-difference-between-increasing-elements/

Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.



Example 1:

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
Example 2:

Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].
Example 3:

Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.


Constraints:

n == nums.length
2 <= n <= 1000
1 <= nums[i] <= 109
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 66 ms, faster than 53.12% of Python3 online submissions for Maximum Difference Between Increasing Elements.
# Memory Usage: 14.6 MB, less than 9.06% of Python3 online submissions for Maximum Difference Between Increasing Elements.
# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         mn, maxdiff = nums[0], -1
#         for v in nums[1:]:
#             maxdiff = max(maxdiff, v - mn)
#             mn = min(mn, v)
#         return maxdiff if maxdiff > 0 else -1


# Runtime: 78 ms, faster than 46.62% of Python3 online submissions for Maximum Difference Between Increasing Elements.
# Memory Usage: 14.5 MB, less than 9.06% of Python3 online submissions for Maximum Difference Between Increasing Elements.
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = reduce(lambda res, v: (max(res[0], v - res[1]), min(res[1], v)), nums[1:], (-1, nums[0]))[0]
        return maxdiff if maxdiff > 0 else -1


tests = [
    [[7,1,5,4], 4],
    [[9,4,3,2], -1],
    [[1,5,2,10], 9],

    [[999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15], -1]
]

run_functional_tests(Solution().maximumDifference, tests)