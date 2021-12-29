"""
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Common.FunctionalUtils import in_place_to_function
from Common.Leetcode import ListNode
from Common.ObjectTestingUtils import convert_test_params_to_lists, run_functional_tests


# Runtime: 88 ms, faster than 85.55% of Python3 online submissions for Reorder List.
# Memory Usage: 23.4 MB, less than 16.26% of Python3 online submissions for Reorder List.
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def middle(head: ListNode) -> ListNode:
            p1, p2 = head, head
            while p2:
                p2 = p2.next
                if not p2:
                    break
                p1 = p1.next
                p2 = p2.next
            return p1

        def reverse(head: ListNode) -> ListNode:
            prev = None
            while head:
                nx = head.next
                head.next = prev
                prev = head
                head = nx
            return prev

        def pairwise_merge(head: ListNode, tail: ListNode):
            p1, p2 = head, tail
            while p1:
                nx1 = p1.next
                nx2 = p2.next if p2 else None
                if p2:
                    p1.next = p2
                    p2.next = nx1

                p1, p2 = nx1, nx2

        if not head or not head.next:
            return
        mid = middle(head)
        tail = mid.next
        mid.next = None
        tail = reverse(tail)
        pairwise_merge(head, tail)


tests = [
    [[1,2,3,4], [1,4,2,3]],
    [[1,2,3,4,5], [1,5,2,4,3]]
]

run_functional_tests(in_place_to_function(Solution().reorderList), convert_test_params_to_lists(tests))
