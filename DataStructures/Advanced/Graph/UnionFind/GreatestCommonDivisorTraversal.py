"""
https://leetcode.com/problems/greatest-common-divisor-traversal/description/?envType=daily-question&envId=2024-02-25

You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.



Example 1:

Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
Example 2:

Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
Example 3:

Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# https://leetcode.com/problems/greatest-common-divisor-traversal/editorial/?envType=daily-question&envId=2024-02-25
# class UnionFind:
#
#     def __init__(self, n):
#         self.p = list(range(n))
#         self.rank = [1] * n
#
#     def get(self, x):
#         while x != self.p[x]:
#             x = self.p[x]
#         return x
#
#     def connect(self, x, y):
#         x, y = self.get(x), self.get(y)
#         if x == y:
#             return
#         if self.rank[x] > self.rank[y]:
#             x, y = y, x
#         self.p[x] = y
#         self.rank[y] += self.rank[x]
#
#
# class Solution:
#     def canTraverseAllPairs(self, nums: List[int]) -> bool:
#         MAX = 10 ** 5
#         N = len(nums)
#         has = [0] * (MAX+1)
#         for x in nums:
#             has[x] = True
#         if N == 1:
#             return True
#         if has[1]:
#             return False
#         sieve = [0] * (MAX+1)
#         for d in range(2, MAX+1):
#             if sieve[d] == 0:
#                 for v in range(d, MAX+1, d):
#                     sieve[v] = d
#         union = UnionFind(2 * MAX + 2)
#         for x in nums:
#             val = x
#             while val > 1:
#                 prime = sieve[val]
#                 root = prime + MAX
#                 if union.get(root) != union.get(x):
#                     union.connect(root, x)
#                 while val % prime == 0:
#                     val //= prime
#         cnt = 0
#         for i in range(2, MAX+1):
#             if has[i] and union.get(i) == i:
#                 cnt += 1
#         return cnt == 1



# Runtime
# 816
# ms
# Beats
# 84.38%
# of users with Python3
# Memory
# 35.99
# MB
# Beats
# 18.75%
# of users with Python3
class UnionFind:

    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [1] * n

    def get(self, x):
        while x != self.p[x]:
            x = self.p[x]
        return x

    def connect(self, x, y):
        x, y = self.get(x), self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        self.p[x] = y
        self.rank[y] += self.rank[x]


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        MAX = max(nums)
        N = len(nums)
        has = set()
        if N == 1:
            return True
        for x in nums:
            has.add(x)
        if 1 in has:
            return False
        sieve = [0] * (MAX+1)
        for d in range(2, MAX+1):
            if sieve[d] == 0:
                for v in range(d, MAX+1, d):
                    sieve[v] = d
        union = UnionFind(2 * MAX + 2)
        for x in nums:
            val = x
            while val > 1:
                prime = sieve[val]
                root = prime + MAX
                if union.get(root) != union.get(x):
                    union.connect(root, x)
                while val % prime == 0:
                    val //= prime
        cnt = 0
        for i in range(2, MAX+1):
            if i in has and union.get(i) == i:
                cnt += 1
        return cnt == 1


tests = [
    [[2,3,6], True],
    [[3,9,5], False],
    [[4,3,12,8], True],
    [[99,35,56,90,99,66,30,63,14,15,88,84,13,84,42,66,44,70,63,90,90,90,55,70,77,100,60,21,30,60,70,10,30,60,84,100,10,28,40,65,70,90,99,45,70,30,70,35,21,26,70,66,42,20,42,30,70,70,30,90,70,15,70,75,55,66,55,55,70,78,42,90,30,70,77,15,90,66,55,84,35,75,55,26,52,90,14,96,52,35,66], True],
    [[66,11,26,42,84,60,35,99,77,88,63,75,90,42,99,70,78,98,91,30,55,40,90,65,63,35,55,30,70,99,60,30,75,66,70,70,78,90,21,90,78,12,42,42,70,60,15,70,82,10,56,91,22,10,84,47,40,60,80,77,15,98,70,42,70,70,77,66,30,90,60,66,10,70,77,70,30,66,77,98,60,28,28,30,60,90,60,78,60], False],
    [[90,35,90,91,53,77,78,98,78,66,84,90,84,10,45,42,60,39,42,70,70,30,98,18,60,66,42,77,84,99,90,66,45,88,15,39,21,30,55,22,12,90,77,98,70,56,66,77,14,45,84,90,66,30,21,34,91,45,90,63,70,78,75,70,28,56,84,48,60,15,10,15,78,15,60,70,30,90,45,50,45,66,70,60,99,60,66,35,60,52,60,98,63,20,84,35,30,30,50], False],
]

run_functional_tests(Solution().canTraverseAllPairs, tests)
