"""
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/?envType=daily-question&envId=2024-03-12

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.



(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]


Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists
from Common.ObjectTestingUtils import run_functional_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# WRONG
# class Solution:
#     def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         root = ListNode(0)
#         root.next = head
#         node = head
#         val = 0
#         prefixes = {0: root}
#         while node:
#             val += node.val
#             if val in prefixes:
#                 prev2 = prefixes[val]
#                 prev2.next = node.next
#             else:
#                 prefixes[val] = node
#             node = node.next
#         if root.next and root.next.val == 0:
#             return None
#         return root.next


# Runtime
# 66
# ms
# Beats
# 13.55%
# of users with Python3
# Memory
# 16.81
# MB
# Beats
# 53.78%
# of users with Python3
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/editorial/?envType=daily-question&envId=2024-03-12
# class Solution:
#     def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         root = ListNode(0, head)
#         start = root
#         while start:
#             prefix_sum = 0
#             end = start.next
#             while end:
#                 prefix_sum += end.val
#                 if prefix_sum == 0:
#                     start.next = end.next
#                 end = end.next
#             start = start.next
#         return root.next


# Runtime
# 40
# ms
# Beats
# 76.49%
# of users with Python3
# Memory
# 16.92
# MB
# Beats
# 29.48%
# of users with Python3
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/editorial/?envType=daily-question&envId=2024-03-12
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {0: front}
        while current:
            prefix_sum += current.val
            prefix_sum_to_node[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = front
        while current:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next

        return front.next


tests = [
    [[1,3,2,-3,-2,5,5,-5,1], [1,5,1]],
    [[0,1,-1], []],
    [[1,-1], []],
    [[0,0], []],
    [[0,0,0], []],
    [[1,2,-3,3,1], [3,1]],
    [[1,2,3,-3,4], [1,2,4]],
    [[1,2,3,-3,-2], [1]],
]

run_functional_tests(Solution().removeZeroSumSublists, convert_test_params_to_lists(tests))
