"""
https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 527 ms, faster than 44.83% of Python3 online submissions for Sort List.
# Memory Usage: 30 MB, less than 91.34% of Python3 online submissions for Sort List.
# https://leetcode.com/submissions/detail/190561231/
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         s, f = head, head.next
#         while f and f.next:
#             s = s.next
#             f = f.next.next
#         list1, list2 = head, s.next
#         s.next = None
#
#         def merge(h1, h2):
#             dummy = ListNode(0)
#             current = dummy
#             while h1 and h2:
#                 if h1.val < h2.val:
#                     current.next = h1
#                     h1 = h1.next
#                 else:
#                     current.next = h2
#                     h2 = h2.next
#                 current = current.next
#             while h1:
#                 current.next = h1
#                 h1 = h1.next
#                 current = current.next
#             while h2:
#                 current.next = h2
#                 h2 = h2.next
#                 current = current.next
#             return dummy.next
#
#         return merge(self.sortList(list1), self.sortList(list2))


# Runtime: 477 ms, faster than 46.66% of Python3 online submissions for Sort List.
# Memory Usage: 30 MB, less than 60.60% of Python3 online submissions for Sort List.
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#
#         def get_mid(head: ListNode) -> ListNode:
#             s, f = head, head.next
#             while f and f.next:
#                 s = s.next
#                 f = f.next.next
#             return s
#
#         def merge(h1, h2):
#             dummy = ListNode(0)
#             current = dummy
#             while h1 and h2:
#                 if h1.val < h2.val:
#                     current.next = h1
#                     h1 = h1.next
#                 else:
#                     current.next = h2
#                     h2 = h2.next
#                 current = current.next
#             while h1:
#                 current.next = h1
#                 h1 = h1.next
#                 current = current.next
#             while h2:
#                 current.next = h2
#                 h2 = h2.next
#                 current = current.next
#             return dummy.next
#
#         mid = get_mid(head)
#         list1, list2 = head, mid.next
#         mid.next = None
#
#         return merge(self.sortList(list1), self.sortList(list2))


# https://leetcode.com/problems/sort-list/solution/
# Runtime: 603 ms, faster than 23.17% of Python3 online submissions for Sort List.
# Memory Usage: 30 MB, less than 87.57% of Python3 online submissions for Sort List.
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def get_count(head: ListNode) -> int:
            cnt = 0
            while head:
                head = head.next
                cnt += 1
            return cnt

        next_sub_list = ListNode(0)
        tail = ListNode(0)

        def split(start: ListNode, size: int) -> ListNode:
            nonlocal next_sub_list
            mid_prev, end = start, start.next
            for index in range(1, size):
                if not mid_prev.next and not end.next:
                    break
                if end.next:
                    end = end.next.next or end.next
                if mid_prev.next:
                    mid_prev = mid_prev.next
            mid = mid_prev.next
            next_sub_list = end.next
            mid_prev.next = None
            end.next = None
            return mid

        def merge(list1: ListNode, list2: ListNode):
            nonlocal tail
            dummy = ListNode(0)
            new_tail = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    new_tail.next = list1
                    list1 = list1.next
                    new_tail = new_tail.next
                else:
                    new_tail.next = list2
                    list2 = list2.next
                    new_tail = new_tail.next
            new_tail.next = list1 or list2
            while new_tail.next:
                new_tail = new_tail.next
            tail.next = dummy.next
            tail = new_tail

        n = get_count(head)
        start = head
        dummy = ListNode(0)

        size = 1
        while size < n:
            tail = dummy
            while start:
                if not start.next:
                    tail.next = start
                    break
                mid = split(start, size)
                merge(start, mid)
                start = next_sub_list
            start = dummy.next

            size *= 2

        return dummy.next


tests = [
    [[4,2,1,3], [1,2,3,4]],
    [[-1,5,3,4,0], [-1,0,3,4,5]],
    [[], []]
]

run_functional_tests(Solution().sortList, convert_test_params_to_lists(tests))
