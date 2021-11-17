"""
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.



Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]


Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 105
-105 <= nums[i], ui, vi <= 105
There exists some nums that has adjacentPairs as its pairs.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1220 ms, faster than 52.17% of Python3 online submissions for Restore the Array From Adjacent Pairs.
# Memory Usage: 68.6 MB, less than 42.24% of Python3 online submissions for Restore the Array From Adjacent Pairs.
# class Solution:
#     def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
#         mp = defaultdict(list)
#         cnt = defaultdict(int)
#         single = set()
#         for a, b in adjacentPairs:
#             mp[a].append(b)
#             mp[b].append(a)
#             cnt[a] += 1
#             cnt[b] += 1
#             if cnt[a] == 1:
#                 single.add(a)
#             elif cnt[a] == 2:
#                 single.remove(a)
#             if cnt[b] == 1:
#                 single.add(b)
#             elif cnt[b] == 2:
#                 single.remove(b)
#         start, end = min(single), max(single)
#         current = start
#         result = [start]
#         visited = {start}
#         while current != end:
#             for nxt in mp[current]:
#                 if nxt in visited:
#                     continue
#                 current = nxt
#                 visited.add(current)
#             result.append(current)
#
#         return result


# Runtime: 1128 ms, faster than 67.31% of Python3 online submissions for Restore the Array From Adjacent Pairs.
# Memory Usage: 63 MB, less than 69.14% of Python3 online submissions for Restore the Array From Adjacent Pairs.
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/discuss/1558676/Python3-Fast-and-Easy
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        single = set()
        for a, b in adjacentPairs:
            mp[a].append(b)
            mp[b].append(a)
            if a not in single:
                single.add(a)
            else:
                single.remove(a)
            if b not in single:
                single.add(b)
            else:
                single.remove(b)
        start, end = min(single), max(single)
        prev = start
        current = start
        result = [start]
        while current != end:
            for nxt in mp[current]:
                if nxt != prev:
                    current = nxt
                    break
            prev = result[-1]
            result.append(current)

        return result


tests = [
    [[[2,1],[3,4],[3,2]], [1,2,3,4]],
    [[[4,-2],[1,4],[-3,1]], [-2,4,1,-3]],
    [[[100000,-100000]], [100000,-100000]]
]


def check(test, result):
    return test[-1] == result or test[-1] == list(reversed(result))


run_functional_tests(Solution().restoreArray, tests, custom_check=check)
