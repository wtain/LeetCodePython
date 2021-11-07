"""
https://leetcode.com/problems/next-greater-node-in-linked-list/

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.



Example 1:


Input: head = [2,1,5]
Output: [5,5,0]
Example 2:


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]


Constraints:

The number of nodes in the list is n.
1 <= n <= 104
1 <= Node.val <= 109
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List

from Common.Leetcode import ListNode
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
#
#         def reverse(head: ListNode) -> ListNode:
#             prev, curr = None, head
#             while curr:
#                 next = curr.next
#                 curr.next = prev
#                 prev, curr = curr, next
#             return prev
#
#         result = []
#         r = reverse(head)
#         mx = 0
#         while r:
#             if r.val < mx:
#                 result.append(mx)
#             else:
#                 result.append(0)
#             mx = max(mx, r.val)
#             r = r.next
#
#         return result[::-1]


# Runtime: 324 ms, faster than 68.66% of Python3 online submissions for Next Greater Node In Linked List.
# Memory Usage: 18.7 MB, less than 33.33% of Python3 online submissions for Next Greater Node In Linked List.
# https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/1554340/Python3-Two-version-of-solutions-with-using-stack
# class Solution:
#     def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
#         result, st, idx = [], [], 0
#         while head:
#             result.append(0)
#
#             while st and st[-1][0] < head.val:
#                 _, index = st.pop()
#                 result[index] = head.val
#
#             st.append((head.val, idx))
#             idx += 1
#             head = head.next
#
#         return result


# Runtime: 320 ms, faster than 75.83% of Python3 online submissions for Next Greater Node In Linked List.
# Memory Usage: 18.5 MB, less than 81.01% of Python3 online submissions for Next Greater Node In Linked List.
# https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/1554340/Python3-Two-version-of-solutions-with-using-stack
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        lst, st, res = [], [], []
        while head:
            lst.append(head.val)
            head = head.next

        for i in range(len(lst)-1, -1, -1):
            max_prev = 0
            while st and st[-1] <= lst[i]:
                st.pop()

            if st:
                max_prev = st[-1]

            res.append(max_prev)
            st.append(lst[i])

        return res[::-1]


tests = [
    [build_list([2,1,5]), [5,5,0]],
    [build_list([2,7,4,3,5]), [7,0,5,5,0]],

    [build_list([1,7,5,1,9,2,5,1]), [7,9,9,9,0,5,0,0]]
]

run_functional_tests(Solution().nextLargerNodes, tests)
