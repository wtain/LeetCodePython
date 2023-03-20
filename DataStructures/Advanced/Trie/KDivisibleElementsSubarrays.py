"""
https://leetcode.com/problems/k-divisible-elements-subarrays/

Given an integer array nums and two integers k and p, return the number of distinct subarrays which have at most k elements divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.



Example 1:

Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11
Explanation:
The elements at indices 0, 3, and 4 are divisible by p = 2.
The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation:
All element of nums are divisible by p = 1.
Also, every subarray of nums will have at most 4 elements that are divisible by 1.
Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.


Constraints:

1 <= nums.length <= 200
1 <= nums[i], p <= 200
1 <= k <= nums.length


Follow up:

Can you solve this problem in O(n2) time complexity?
"""
import collections
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 3757 ms
# Beats
# 5.10%
# Memory
# 21.3 MB
# Beats
# 81.39%
# class Solution:
#     def countDistinct(self, nums: List[int], k: int, p: int) -> int:
#         n = len(nums)
#         i1 = 0
#         np = 0
#         Trie = lambda: collections.defaultdict(Trie)
#         trie = Trie()
#
#         total = 0
#
#         def add_suffix(suffix):
#             nonlocal trie, total
#             node = trie
#             suffix += ['$']
#             for c in suffix:
#                 if c == '$' and c not in node:
#                     total += 1
#                 node = node[c]
#
#         for i2 in range(n):
#             if nums[i2] % p == 0:
#                 np += 1
#             while np > k and i1 <= i2:
#                 if nums[i1] % p == 0:
#                     np -= 1
#                 i1 += 1
#             suffix = []
#             for i in range(i2, i1-1, -1):
#                 suffix = [nums[i]] + suffix
#                 add_suffix(suffix.copy())
#         return total

# Runtime
# 346 ms
# Beats
# 72.99%
# Memory
# 21 MB
# Beats
# 81.39%
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        i1 = 0
        np = 0

        hashes = set()

        for i2 in range(n):
            if nums[i2] % p == 0:
                np += 1
            while np > k and i1 <= i2:
                if nums[i1] % p == 0:
                    np -= 1
                i1 += 1
            suffix = []
            hash = 0
            for i in range(i2, i1-1, -1):
                hash = hash * 1000001 + nums[i]
                suffix = [nums[i]] + suffix
                hashes.add(hash)
        return len(hashes)


tests = [
    [[2,3,3,2,2], 2, 2, 11],
    [[1,2,3,4], 4, 1, 10],
]

run_functional_tests(Solution().countDistinct, tests)
