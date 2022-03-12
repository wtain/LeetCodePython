"""
https://leetcode.com/problems/delete-and-earn/

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.



Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 92 ms, faster than 44.01% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.3 MB, less than 54.80% of Python3 online submissions for Delete and Earn.
# https://leetcode.com/submissions/detail/360360527/
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: -x)
        n = len(nums)
        dp = [[0] * 2 for _ in range(n+1)]
        prevv, k, i = -1, 0, 0
        while i < n:
            v0, v1, ci, j = dp[k][0], dp[k][1], nums[i], i
            si = 0
            while j < n and nums[j] == nums[i]:
                si += ci
                j += 1
            if nums[i] == nums[0] or nums[i] + 1 != prevv:
                dp[k+1][1] = si + max(v0, v1)
            else:
                dp[k+1][1] = max(v0 + si, v1)
            dp[k+1][0] = max(v0, v1)
            prevv = ci
            i = j
            k += 1
        return max(dp[k][0], dp[k][1])


# Runtime: 64 ms, faster than 77.59% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.6 MB, less than 26.77% of Python3 online submissions for Delete and Earn.
# https://leetcode.com/problems/delete-and-earn/solution/
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(num, max_number)

        max_points = [0] * (max_number + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])

        return max_points[max_number]


tests = [
    [[3,4,2], 6],
    [[2,2,3,3,3,4], 9]
]

run_functional_tests(Solution().deleteAndEarn, tests)
