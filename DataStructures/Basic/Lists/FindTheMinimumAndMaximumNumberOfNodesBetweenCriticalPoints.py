"""
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2024-07-05

A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].



Example 1:


Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].
Example 2:


Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
Example 3:


Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.


Constraints:

The number of nodes in the list is in the range [2, 105].
1 <= Node.val <= 105
"""
import math
from typing import Optional, List

from Common.DataTypes.Leetcode import ListNode
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 373
# ms
# Beats
# 25.09%
# Analyze Complexity
# Memory
# 44.15
# MB
# Beats
# 91.25%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
#         pos = 0
#         prev, curr = None, head
#         extremes = []
#         while curr:
#             if prev and curr.next:
#                 if prev.val < curr.val and curr.next.val < curr.val or \
#                    prev.val > curr.val and curr.next.val > curr.val:
#                     extremes.append(pos)
#             pos += 1
#             prev = curr
#             curr = curr.next
#         if len(extremes) < 2:
#             return [-1, -1]
#         mn = mx = extremes[-1] - extremes[0]
#         for i in range(1, len(extremes)):
#             diff = extremes[i] - extremes[i-1]
#             mn = min(mn, diff)
#         return [mn, mx]

# Runtime
# 369
# ms
# Beats
# 31.56%
# Analyze Complexity
# Memory
# 44.41
# MB
# Beats
# 30.04%
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos = 0
        prev, curr = None, head
        prev_critical = first_critical = -1
        mx = -1
        mn = math.inf
        while curr:
            if prev and curr.next:
                if prev.val < curr.val and curr.next.val < curr.val or \
                   prev.val > curr.val and curr.next.val > curr.val:
                    if first_critical == -1:
                        first_critical = pos
                    else:
                        mx = pos - first_critical
                    if prev_critical != -1:
                        mn = min(mn, pos - prev_critical)
                    prev_critical = pos
            pos += 1
            prev = curr
            curr = curr.next
        if mx == -1:
            return [-1, -1]
        return [mn, mx]


tests = [
    [[3,1], [-1,-1]],
    [[5,3,1,2,5,1,2], [1,3]],
    [[1,3,2,2,3,2,2,2,7], [3,3]],
]

run_functional_tests(Solution().nodesBetweenCriticalPoints, convert_test_params_to_lists(tests, indexes=[0]))
