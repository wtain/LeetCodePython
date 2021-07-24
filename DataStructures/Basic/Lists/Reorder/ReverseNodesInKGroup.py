"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3818/
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]


Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List

from Common.Leetcode import ListNode
from Common.ListUtils import printList
from Common.ObjectTestingUtils import run_functional_tests, convert_test_params_to_lists


# Runtime: 40 ms, faster than 98.03% of Python3 online submissions for Reverse Nodes in k-Group.
# Memory Usage: 15.2 MB, less than 76.72% of Python3 online submissions for Reverse Nodes in k-Group.
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse(node: ListNode, k: int) -> List[ListNode]:
            prev, curr, next = None, node, None
            for _ in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            node.next = curr
            return [prev, curr]

        def has_k(node: ListNode, k: int) -> bool:
            for _ in range(k):
                if not node:
                    return False
                node = node.next
            return True

        new_head = None

        prev, curr, next = None, head, None
        while curr:
            if has_k(curr, k):
                k_prev, k_curr = reverse(curr, k)
                if not new_head:
                    new_head = k_prev
                if prev:
                    prev.next = k_prev
                prev = curr
                curr = k_curr
            else:
                break

            # printList(new_head)

        if not new_head:
            new_head = head

        return new_head


tests = [
    [[1,2,3,4,5], 2, [2,1,4,3,5]],
    [[1,2,3,4,5], 3, [3,2,1,4,5]],
    [[1,2,3,4,5], 1, [1,2,3,4,5]],
    [[1], 1, [1]]
]

run_functional_tests(Solution().reverseKGroup, convert_test_params_to_lists(tests, [0, 2]))