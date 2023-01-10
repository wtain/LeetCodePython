"""
https://leetcode.com/problems/largest-values-from-labels/

There is a set of n items. You are given two integer arrays values and labels where the value and the label of the ith element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

Choose a subset s of the n elements such that:

The size of the subset s is less than or equal to numWanted.
There are at most useLimit items with the same label in s.
The score of a subset is the sum of the values in the subset.

Return the maximum score of a subset s.



Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth items.
Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third items.
Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
Output: 16
Explanation: The subset chosen is the first and fourth items.


Constraints:

n == values.length == labels.length
1 <= n <= 2 * 104
0 <= values[i], labels[i] <= 2 * 104
1 <= numWanted, useLimit <= n
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 133 ms
# Beats
# 96.77%
# Memory
# 19.3 MB
# Beats
# 52.7%
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = [(value, label) for value, label in zip(values, labels)]
        items.sort(key=lambda item: -item[0])
        used = 0
        score = 0
        counts = defaultdict(int)
        for value, label in items:
            if used == numWanted:
                break
            if counts[label] == useLimit:
                continue
            used += 1
            counts[label] += 1
            score += value
        return score


tests = [
    [[5,4,3,2,1], [1,1,2,2,3], 3, 1, 9],
    [[5,4,3,2,1], [1,3,3,3,2], 3, 2, 12],
    [[9,8,8,7,6], [0,0,0,1,1], 3, 1, 16],
]

run_functional_tests(Solution().largestValsFromLabels, tests)
