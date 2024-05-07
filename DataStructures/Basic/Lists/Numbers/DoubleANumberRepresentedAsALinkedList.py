"""
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.



Example 1:


Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:


Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.


Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
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


# Runtime
# 231
# ms
# Beats
# 71.83%
# of users with Python3
# Memory
# 19.22
# MB
# Beats
# 86.07%
# of users with Python3
# class Solution:
#     def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         def reverse(head):
#             prev = None
#             curr = head
#             while curr:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp
#             return prev
#
#         rev = reverse(head)
#         carry = 0
#         curr = rev
#         while curr:
#             digit = 2*curr.val+carry
#             carry = 1 if digit >= 10 else 0
#             curr.val = digit % 10
#             curr = curr.next
#         rev = reverse(rev)
#         if carry:
#             h1 = ListNode(carry)
#             h1.next = rev
#             rev = h1
#
#         return rev


# Runtime
# 207
# ms
# Beats
# 98.44%
# of users with Python3
# Memory
# 19.35
# MB
# Beats
# 64.32%
# of users with Python3
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/editorial/?envType=daily-question&envId=2024-05-07
# class Solution:
#     def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head
#         while curr:
#             v = curr.val * 2
#             if v < 10:
#                 curr.val = v
#             elif prev:
#                 curr.val = v % 10
#                 prev.val += 1
#             else:
#                 head = ListNode(1, curr)
#                 curr.val = v % 10
#             prev = curr
#             curr = curr.next
#         return head


# Runtime
# 205
# ms
# Beats
# 99.06%
# of users with Python3
# Memory
# 19.29
# MB
# Beats
# 86.07%
# of users with Python3
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/editorial/?envType=daily-question&envId=2024-05-07
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        curr = head
        while curr:
            curr.val = curr.val * 2 % 10
            if curr.next and curr.next.val > 4:
                curr.val += 1
            curr = curr.next
        return head


tests = [
    [[1,8,9], [3,7,8]],
    [[9,9,9], [1,9,9,8]],
]

run_functional_tests(Solution().doubleIt, convert_test_params_to_lists(tests))
