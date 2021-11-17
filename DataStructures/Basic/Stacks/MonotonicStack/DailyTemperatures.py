"""
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1228 ms, faster than 75.60% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 25.5 MB, less than 46.32% of Python3 online submissions for Daily Temperatures.
# Runtime: 1224 ms, faster than 76.72% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 25.5 MB, less than 46.13% of Python3 online submissions for Daily Temperatures.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, result = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                result[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return result


tests = [
    [[73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]],
    [[30,40,50,60], [1,1,1,0]],
    [[30,60,90], [1,1,0]]
]

run_functional_tests(Solution().dailyTemperatures, tests)
