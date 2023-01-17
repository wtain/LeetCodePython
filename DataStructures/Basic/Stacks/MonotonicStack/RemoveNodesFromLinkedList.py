"""
https://leetcode.com/problems/remove-nodes-from-linked-list/

You are given the head of a linked list.

Remove every node which has a node with a strictly greater value anywhere to the right side of it.

Return the head of the modified linked list.



Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.


Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""
from typing import Optional

from numpy import Inf

from Common.DataTypes.Leetcode import ListNode
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists
from Common.ObjectTestingUtils import run_functional_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Runtime
# 1128 ms
# Beats
# 98.97%
# Memory
# 61 MB
# Beats
# 73.2%
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         stack = []
#         while head:
#             while stack and stack[-1].val < head.val:
#                 stack.pop()
#             stack.append(head)
#             head = head.next
#         for i in range(1, len(stack)):
#             stack[i-1].next = stack[i]
#         return stack[0]


# Runtime
# 1372 ms
# Beats
# 84.12%
# Memory
# 78.4 MB
# Beats
# 22.58%
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [ListNode(Inf)]
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack[-1].next = head
            stack.append(head)
            head = head.next
        return stack[0].next


tests = [
    [[5,2,13,3,8], [13,8]],
    [[1,1,1,1], [1,1,1,1]],
]

run_functional_tests(Solution().removeNodes, convert_test_params_to_lists(tests))
