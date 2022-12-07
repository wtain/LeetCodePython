"""
https://leetcode.com/problems/random-flip-matrix/

There is an m x n binary grid matrix with all the values set 0 initially. Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely to be returned.

Optimize your algorithm to minimize the number of calls made to the built-in random function of your language and optimize the time and space complexity.

Implement the Solution class:

Solution(int m, int n) Initializes the object with the size of the binary matrix m and n.
int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j] == 0 and flips it to 1.
void reset() Resets all the values of the matrix to be 0.


Example 1:

Input
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
Output
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

Explanation
Solution solution = new Solution(3, 1);
solution.flip();  // return [1, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
solution.flip();  // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
solution.flip();  // return [0, 0], Based on the previously returned indices, only [0,0] can be returned.
solution.reset(); // All the values are reset to 0 and can be returned.
solution.flip();  // return [2, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.


Constraints:

1 <= m, n <= 104
There will be at least one free cell for each call to flip.
At most 1000 calls will be made to flip and reset.
"""
import copy
import random
from itertools import product
from random import shuffle
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# TLE
# class Solution:
#
#     def __init__(self, m: int, n: int):
#         self.cells = []
#         self.m = m
#         self.n = n
#         self.reset()
#
#     def flip(self) -> List[int]:
#         i, j = self.cells.pop()
#         return [i, j]
#
#     def reset(self) -> None:
#         self.cells = [[i, j] for i, j in product(range(self.m), range(self.n))]
#         shuffle(self.cells)


# TLE
# class Solution:
#
#     def __init__(self, m: int, n: int):
#         self.cells = []
#         self.m = m
#         self.n = n
#         self.initial = [[i, j] for i, j in product(range(self.m), range(self.n))]
#         self.reset()
#
#     def flip(self) -> List[int]:
#         i, j = self.cells.pop()
#         return [i, j]
#
#     def reset(self) -> None:
#         self.cells = copy.copy(self.initial)
#         shuffle(self.cells)


# Runtime
# 183 ms
# Beats
# 12.7%
# Memory
# 14.5 MB
# Beats
# 22.41%
# https://leetcode.com/problems/random-flip-matrix/solutions/154072/python-solution-using-set/
# class Solution:
#
#     def __init__(self, m: int, n: int):
#         self.m, self.n = m, n
#         self.flipped = set()
#
#     def flip(self) -> List[int]:
#         while True:
#             m, n = random.randint(0, self.m-1), random.randint(0, self.n-1)
#             if (m, n) not in self.flipped:
#                 self.flipped.add((m, n))
#                 return [m, n]
#
#     def reset(self) -> None:
#         self.flipped = set()


# TLE?
# https://leetcode.com/problems/random-flip-matrix/solutions/154424/least-number-of-random-call-using-set-with-explanation/
# class Solution:
#
#     def __init__(self, m: int, n: int):
#         self.m, self.n = m, n
#         self.used = set()
#
#     def flip(self) -> List[int]:
#         v = random.randint(0, self.n * self.m - 1 - len(self.used))
#         if v in self.used:
#             i = self.n * self.m - 1
#             effective = self.n * self.m - len(self.used) - v
#
#             while effective != 0:
#                 if i not in self.used:
#                     effective -= 1
#                     i -= 1
#
#                 v = i + 1
#         self.used.add(v)
#         return [v // self.n, v % self.n]
#
#     def reset(self) -> None:
#         self.used = set()


# Runtime
# 145 ms
# Beats
# 30.46%
# Memory
# 14.5 MB
# Beats
# 22.41%
# https://leetcode.com/problems/random-flip-matrix/solutions/155329/reservoir-sampling-optimal-solution/
class ReservoirSampling:
    def __init__(self, n):
        self.n = n
        self.build()

    def build(self):
        self.m = {}
        self.l = self.n

    def get_next(self):
        self.l -= 1
        r = random.randint(0, self.l)
        v = self.m.get(r, r)
        self.m[r] = self.m.get(self.l, self.l)
        return v

    def reset(self):
        self.build()

class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.rs = ReservoirSampling(m*n)

    def flip(self) -> List[int]:
        n = self.rs.get_next()
        return self.n2rc(n)

    def n2rc(self, n):
        return [n // self.n, n % self.n]

    def reset(self) -> None:
        self.rs.reset()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()


tests = [
    [
        ["Solution", "flip", "flip", "flip", "reset", "flip"],
        [[3, 1], [], [], [], [], []],
        [null, [1, 0], [2, 0], [0, 0], null, [2, 0]]
    ]
]

run_object_tests(tests, cls=Solution)
