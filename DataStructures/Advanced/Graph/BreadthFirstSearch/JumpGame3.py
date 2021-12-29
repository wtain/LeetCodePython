"""
https://leetcode.com/problems/jump-game-iii/

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.


Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 284 ms, faster than 93.25% of Python3 online submissions for Jump Game III.
# Memory Usage: 21 MB, less than 61.97% of Python3 online submissions for Jump Game III.
# Runtime: 292 ms, faster than 82.30% of Python3 online submissions for Jump Game III.
# Memory Usage: 21.2 MB, less than 54.48% of Python3 online submissions for Jump Game III.
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        level = [start]
        n = len(arr)
        visted = set()
        while level:
            next_level = []
            for i in level:
                visted.add(i)
                if arr[i] == 0:
                    return True
                v1, v2 = i - arr[i], i + arr[i]
                if 0 <= v1 < n and v1 not in visted:
                    next_level.append(v1)
                if 0 <= v2 < n and v2 not in visted:
                    next_level.append(v2)
            level = next_level
        return False


tests = [
    [[4,2,3,0,3,1,2], 5, True],
    [[4,2,3,0,3,1,2], 0, True],
    [[3,0,2,1,2], 2, False]
]

run_functional_tests(Solution().canReach, tests)
