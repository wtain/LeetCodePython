"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/

You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).



Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.


Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.
"""
import heapq
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 748 ms, faster than 33.19% of Python3 online submissions for Split Array into Consecutive Subsequences.
# Memory Usage: 16 MB, less than 5.43% of Python3 online submissions for Split Array into Consecutive Subsequences.
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # set of
        subseqs = defaultdict(list) # dictionary of heaps
        num_less_3 = 0
        for v in nums:
            v1 = v-1
            if len(subseqs[v1]) == 0:
                heapq.heappush(subseqs[v], (1, [v]))
                num_less_3 += 1
            else:
                slen, shortest = heapq.heappop(subseqs[v1])
                if slen == 2:
                    num_less_3 -= 1
                shortest.append(v)
                heapq.heappush(subseqs[v], (slen+1, shortest))

        return num_less_3 == 0


tests = [
    [[1,2,3,3,4,5], True],
    [[1,2,3,3,4,4,5,5], True],
    [[1,2,3,4,4,5], False]
]

run_functional_tests(Solution().isPossible, tests)