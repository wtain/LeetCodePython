"""
https://leetcode.com/problems/ipo/description/

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.



Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6


Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1080 ms
# Beats
# 52.62%
# Memory
# 39.3 MB
# Beats
# 21.15%
# https://leetcode.com/problems/ipo/solutions/2959870/ipo/
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(c, p) for p,c in zip(profits, capital)]
        projects.sort()
        n = len(projects)
        i = 0
        q = []
        for j in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(q, -projects[i][1])
                i += 1
            if not q:
                break
            w += -heapq.heappop(q)
        return w


tests = [
    [2, 0, [1,2,3], [0,1,1], 4],
    [3, 0, [1,2,3], [0,1,2], 6],
]

run_functional_tests(Solution().findMaximizedCapital, tests)
