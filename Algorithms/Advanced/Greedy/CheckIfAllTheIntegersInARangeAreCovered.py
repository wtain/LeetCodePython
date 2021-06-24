"""
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.



Example 1:

Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
Example 2:

Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.


Constraints:

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 66.67% of Python3 online submissions for Check if All the Integers in a Range Are Covered.
# Memory Usage: 14.2 MB, less than 66.67% of Python3 online submissions for Check if All the Integers in a Range Are Covered.
# class Solution:
#     def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
#         covered = set()
#         for b, e in ranges:
#             for i in range(b, e+1):
#                 if left <= i <= right:
#                     covered.add(i)
#         return len(covered) == right - left + 1


# Runtime: 40 ms, faster than 66.67% of Python3 online submissions for Check if All the Integers in a Range Are Covered.
# Memory Usage: 14.3 MB, less than 66.67% of Python3 online submissions for Check if All the Integers in a Range Are Covered.
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            covered = False
            for b,e in ranges:
                if b <= i <= e:
                    covered = True
                    continue
            if not covered:
                return False
        return True


tests = [
    [[[1,2],[3,4],[5,6]], 2, 5, True],
    [[[1,10],[10,20]], 21, 21, False]
]

run_functional_tests(Solution().isCovered, tests)