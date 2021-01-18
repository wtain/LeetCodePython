"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3608/
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.



Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
from collections import defaultdict
from typing import List, Dict


# TLE
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         counts: Dict[int, int] = {}
#         for x in nums:
#             counts[x] = counts.get(x, 0) + 1
#         res = 0
#         seen = []
#         for x in counts:
#             if x in seen:
#                 continue
#             y = k - x
#             if x == y:
#                 cnt = counts[x] // 2
#             else:
#                 cnt = min(counts.get(x, 0), counts.get(y, 0))
#             seen.append(x)
#             seen.append(y)
#             res += cnt
#         return res

# Runtime: 1104 ms, faster than 5.60% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27.8 MB, less than 8.47% of Python3 online submissions for Max Number of K-Sum Pairs.
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         counts: Dict[int, int] = {}
#         for x in nums:
#             counts[x] = counts.get(x, 0) + 1
#         res = 0
#         seen = set([])
#         for x in counts:
#             if x in seen:
#                 continue
#             y = k - x
#             if x == y:
#                 cnt = counts[x] // 2
#             else:
#                 cnt = min(counts.get(x, 0), counts.get(y, 0))
#             seen.add(x)
#             seen.add(y)
#             res += cnt
#         return res


# Runtime: 680 ms, faster than 66.29% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27.8 MB, less than 8.47% of Python3 online submissions for Max Number of K-Sum Pairs.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(int)
        for x in nums:
            y = k - x
            if d[y] > 0:
                res += 1
                d[y] -= 1
            else:
                d[x] += 1
        return res



tests = [
    ([1,2,3,4], 5, 2),
    ([3,1,3,4,3], 6, 1)
]

for test in tests:
    result = Solution().maxOperations(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))