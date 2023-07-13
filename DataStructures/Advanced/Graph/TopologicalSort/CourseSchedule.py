"""
https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests



# Runtime
# 218 ms
# Beats
# 6.90%
# Memory
# 18.1 MB
# Beats
# 68.82%
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies, dependants = [set() for _ in range(numCourses)], [set() for _ in range(numCourses)]
        taken = set()
        for a, b in prerequisites:
            dependencies[b].add(a)
            dependants[a].add(b)

        while True:
            took_something = False
            for i in range(numCourses):
                if i not in taken and not dependencies[i]:
                    taken.add(i)
                    took_something = True
                    for j in dependants[i]:
                        dependencies[j].remove(i)
            if not took_something:
                break
        return len(taken) == numCourses


tests = [
    [2, [[1,0]], True],
    [2, [[1,0],[0,1]], False],
]

run_functional_tests(Solution().canFinish, tests)
