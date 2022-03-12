"""
https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 65.44% of Python3 online submissions for Rotate List.
# Memory Usage: 13.9 MB, less than 88.66% of Python3 online submissions for Rotate List.
# https://leetcode.com/submissions/detail/138930363/
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def advance(head, k):
            if not head:
                return head
            node = head
            while k:
                k -= 1
                node = node.next
                if not node:
                    node = head
            return node

        def length(head):
            rv = 0
            while head:
                rv += 1
                head = head.next
            return rv

        def get_nth_from_end(head, n):
            current = advance(head, n)
            if not current:
                return None
            while current.next:
                current = current.next
                head = head.next
            return head

        if not head:
            return head
        n = length(head)
        k %= n
        if not k:
            return head
        end = get_nth_from_end(head, k)
        tail = end.next
        if not tail:
            tail = head
        end.next = None
        last = tail
        while last.next:
            last = last.next
        last.next = head
        return tail


tests = [
    [build_list([1]), 1, build_list([1])],
    [build_list([1]), 0, build_list([1])],
    [build_list([1,2,3,4,5]), 2, build_list([4,5,1,2,3])],
    [build_list([0,1,2]), 4, build_list([2,0,1])]
]

run_functional_tests(Solution().rotateRight, tests)
