"""
https://leetcode.com/problems/task-scheduler/description/?envType=daily-question&envId=2024-03-19

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.



Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 340
# ms
# Beats
# 98.34%
# of users with Python3
# Memory
# 17.02
# MB
# Beats
# 79.06%
# of users with Python3
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(reversed(sorted(Counter(tasks).values())))
        ln = 1
        max_cnt = counts[0]
        for i in range(1, len(counts)):
            if counts[i] == max_cnt:
                ln += 1
        space = (n+1) * (max_cnt - 1) + ln
        m = len(tasks)
        return m if space < m else space


tests = [
    [["A","A","A","B","B","B"], 2, 8],
    [["A","C","A","B","D","B"], 1, 6],
    [["A","A","A", "B","B","B"], 3, 10],
]

run_functional_tests(Solution().leastInterval, tests)
