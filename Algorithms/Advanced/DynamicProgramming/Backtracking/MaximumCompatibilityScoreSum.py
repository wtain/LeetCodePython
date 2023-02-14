"""
https://leetcode.com/problems/maximum-compatibility-score-sum/

There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1. The answers of the students are represented by a 2D integer array students where students[i] is an integer array that contains the answers of the ith student (0-indexed). The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array that contains the answers of the jth mentor (0-indexed).

Each student will be assigned to one mentor, and each mentor will have one student assigned to them. The compatibility score of a student-mentor pair is the number of answers that are the same for both the student and the mentor.

For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1], then their compatibility score is 2 because only the second and the third answers are the same.
You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.

Given students and mentors, return the maximum compatibility score sum that can be achieved.



Example 1:

Input: students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
Output: 8
Explanation: We assign students to mentors in the following way:
- student 0 to mentor 2 with a compatibility score of 3.
- student 1 to mentor 0 with a compatibility score of 2.
- student 2 to mentor 1 with a compatibility score of 3.
The compatibility score sum is 3 + 2 + 3 = 8.
Example 2:

Input: students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
Output: 0
Explanation: The compatibility score of any student-mentor pair is 0.


Constraints:

m == students.length == mentors.length
n == students[i].length == mentors[j].length
1 <= m, n <= 8
students[i][k] is either 0 or 1.
mentors[j][k] is either 0 or 1.
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2124 ms
# Beats
# 37.43%
# Memory
# 26.4 MB
# Beats
# 8.94%
# class Solution:
#     def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
#
#         n = len(students)
#         scores = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 for si, mi in zip(students[i], mentors[j]):
#                     scores[i][j] += (si == mi)
#
#         @cache
#         def dp(mask_students: int, mask_mentors: int) -> int:
#             nonlocal n, scores
#             result = 0
#             for i in range(n):
#                 if mask_students & (1 << i):
#                     continue
#                 for j in range(n):
#                     if mask_mentors & (1 << j):
#                         continue
#                     result = max(result, scores[i][j] + dp(mask_students + (1 << i), mask_mentors + (1 << j)))
#             return result
#
#         return dp(0, 0)


# Runtime
# 3280 ms
# Beats
# 25.14%
# Memory
# 16.4 MB
# Beats
# 20.67%
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        n = len(students)
        scores = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for si, mi in zip(students[i], mentors[j]):
                    scores[i][j] += (si == mi)

        dp = [[0] * (1 << n) for _ in range(1 << n)]
        to_visit = [(0, 0)]
        visited = {(0, 0)}
        while to_visit:
            next_level = []
            for mi, mj in to_visit:
                for i in range(n):
                    if mi & (1 << i):
                        continue
                    for j in range(n):
                        if mj & (1 << j):
                            continue
                        dp[mi + (1 << i)][mj + (1 << j)] = max(dp[mi + (1 << i)][mj + (1 << j)], dp[mi][mj] + scores[i][j])
                        if (mi + (1 << i), mj + (1 << j)) not in visited:
                            visited.add((mi + (1 << i), mj + (1 << j)))
                            next_level.append((mi + (1 << i), mj + (1 << j)))
            to_visit = next_level

        return dp[-1][-1]


tests = [
    [
        [[0,0,1,0,0,0,0,0],[1,1,0,1,0,0,0,0],[1,0,0,1,1,0,0,0],[1,0,1,1,1,1,1,0],[1,1,0,1,1,0,1,0],[0,1,0,0,0,1,1,1],[1,0,0,0,1,0,0,1],[1,0,0,1,1,1,0,1]],
        [[1,1,0,0,0,1,0,0],[1,1,1,1,0,1,0,0],[1,0,0,1,1,0,0,1],[1,1,1,0,0,0,1,0],[1,0,0,0,1,0,1,1],[1,0,1,1,0,1,0,0],[1,1,0,1,1,0,1,0],[0,1,0,0,0,1,0,0]],
        49
    ],
    [[[1,1,0],[1,0,1],[0,0,1]], [[1,0,0],[0,0,1],[1,1,0]], 8],
    [[[0,0],[0,0],[0,0]], [[1,1],[1,1],[1,1]], 0],
]

run_functional_tests(Solution().maxCompatibilitySum, tests)
