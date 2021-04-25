"""
https://leetcode.com/problems/random-pick-with-blacklist/
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
import random
from typing import List


# TLE - try Fenwick
# class TreeNode:
#
#     def __init__(self, left: int, right: int):
#         self.range_left = left
#         self.range_right = right
#         self.left = None
#         self.right = None
#         self.cnt = 0
#
#     def isLeaf(self) -> bool:
#         return self.range_left == self.range_right
#
#     def getMid(self) -> int:
#         return self.range_left + (self.range_right+1 - self.range_left) // 2
#
#     def getLeft(self):  # -> TreeNode:
#         if not self.left:
#             self.left = TreeNode(self.range_left, self.getMid() - 1)
#         return self.left
#
#     def getRight(self):  # -> TreeNode:
#         if not self.right:
#             self.right = TreeNode(self.getMid(), self.range_right)
#         return self.right
#
#     def add(self, v: int):
#         # print(self.range_left, self.range_right)
#         self.cnt += 1
#         if not self.isLeaf():
#             if v < self.getMid():
#                 self.getLeft().add(v)
#             else:
#                 self.getRight().add(v)
#
#     def countLess(self, v: int) -> int:
#         if v >= self.getMid():
#             return (self.left.cnt if self.left else 0) + (self.right.countLess(v) if self.right else 0)
#         else:
#             return self.left.countLess(v) if self.left else 0
#
#     def countRange(self, a: int, b: int) -> int:
#         return self.countLess(b) - self.countLess(a)
#
# class SegmentTree:
#
#     def __init__(self, left: int, right: int):
#         self.root = TreeNode(left, right)
#
#     def add(self, v: int):
#         self.root.add(v)
#
#     def getLess(self, v: int) -> int:
#         return self.root.countLess(v)
#
#     def countRange(self, a: int, b: int) -> int:
#         return self.root.countRange(a, b)
#
# class Solution:
#
#     def __init__(self, N: int, blacklist: List[int]):
#         self.N = N
#         self.K = len(blacklist)
#         self.tree = SegmentTree(0, N-1)
#         self.blacklist = set(blacklist)
#         for b in blacklist:
#             self.tree.add(b)
#
#     def count_blacklisted_less(self, r: int) -> int:
#         cnt = 0
#         for b in self.blacklist:
#             if b <= r + cnt:
#                 cnt += 1
#             else:
#                 break
#         return cnt
#
#     def pick(self) -> int:
#         r = random.randint(0, self.N - self.K - 1)
#         # r += self.count_blacklisted_less(r)
#         r_prev = r
#         r += self.tree.getLess(r)
#         while r > r_prev:
#             cnt = self.tree.countRange(r_prev, r)
#             r_prev = r
#             r += cnt
#         while r in self.blacklist:
#             r += 1
#         return r

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()

# Runtime: 360 ms, faster than 71.07% of Python3 online submissions for Random Pick with Blacklist.
# Memory Usage: 25.9 MB, less than 23.14% of Python3 online submissions for Random Pick with Blacklist.
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.B = len(blacklist)

        sechf_iter = iter(set([i for i in range(N-self.B, N)]).difference(blacklist))

        self.mapping = {}
        for b in blacklist:
            if b < N-self.B:
                self.mapping[b] = next(sechf_iter)

    def pick(self) -> int:
        r = random.randint(0, self.N - self.B - 1)
        if r in self.mapping:
            r = self.mapping[r]
        return r


s1 = Solution(1, [])
print(s1.pick())
print(s1.pick())
print(s1.pick())

print()

s2 = Solution(2, [])
print(s2.pick())
print(s2.pick())
print(s2.pick())

print()

s3 = Solution(3, [1])
print(s3.pick())
print(s3.pick())
print(s3.pick())

print()

s4 = Solution(4, [2])
print(s4.pick())
print(s4.pick())
print(s4.pick())

print()

s5 = Solution(5, [2, 1, 0])
print(s5.pick())
print(s5.pick())
print(s5.pick())