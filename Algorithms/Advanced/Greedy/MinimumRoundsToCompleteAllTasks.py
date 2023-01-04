"""
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.



Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2.
- In the second round, you complete 2 tasks of difficulty level 3.
- In the third round, you complete 3 tasks of difficulty level 4.
- In the fourth round, you complete 2 tasks of difficulty level 4.
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.


Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 3125 ms
# Beats
# 5.75%
# Memory
# 28.4 MB
# Beats
# 60.98%
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)                 # Count tasks of each difficulty
        rounds = 0                              # Initialize the number of the required rounds
        for difficulty in counts:               # Iterate over counts per difficulty
            if counts[difficulty] == 1:         # If we only have one task of a given difficulty -
                return -1                       # then we can't complete all the tasks as long as
                                                # we can only take 2 or 3 per round, but not 1
            rounds += counts[difficulty] // 3   # To minimize the number of rounds we will take
                                                # three tasks per round
            if counts[difficulty] % 3:          # If the remainder is not zero (1 or 2), then
                rounds += 1                     # we need an extra round.
                                                # Note: in case of one task remaining we take
                                                # a task from previous round of three tasks and
                                                # so that last round has two tasks
        return rounds                           # Return the number of rounds


tests = [
    [[2,2,3,3,2,4,4,4,4,4], 4],
    [[2,3,3], -1]
]

run_functional_tests(Solution().minimumRounds, tests)
