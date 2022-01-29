"""
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

n == number of nodes in the linked list
0 <= n <= 104
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists


# Runtime: 36 ms, faster than 96.20% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 16.4 MB, less than 56.86% of Python3 online submissions for Odd Even Linked List.
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         odd_head, even_head = ListNode(0), ListNode(0)
#         odd_curr, even_curr = odd_head, even_head
#         odd = True
#         while head:
#             if odd:
#                 odd_curr.next = head
#                 odd_curr = odd_curr.next
#             else:
#                 even_curr.next = head
#                 even_curr = even_curr.next
#             odd = not odd
#             head = head.next
#         even_curr.next = None
#         odd_curr.next = even_head.next
#         return odd_head.next


# Runtime: 36 ms, faster than 96.20% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 16.4 MB, less than 56.86% of Python3 online submissions for Odd Even Linked List.
# https://leetcode.com/problems/odd-even-linked-list/solution/
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


tests = [
    [[1,2,3,4,5], [1,3,5,2,4]],
    [[2,1,3,5,6,4,7], [2,3,6,7,1,5,4]]
]

run_functional_tests(Solution().oddEvenList, convert_test_params_to_lists(tests))
