"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3789/
https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Common.Leetcode import ListNode
from Common.ObjectTestingUtils import run_functional_tests, convert_test_params_to_lists


# Runtime: 28 ms, faster than 86.83% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14.5 MB, less than 39.15% of Python3 online submissions for Reverse Linked List II.
class Solution:

    def reverse(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        curr, prev = head, None
        while curr and n >= 1:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            n -= 1
        head.next = curr
        return prev

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        curr, prev = head, None
        while left > 1 and curr:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        tail = self.reverse(curr, right)
        if not prev:
            return tail
        prev.next = tail
        return head


tests = [
    [
        [1,2,3,4,5], 2, 4,
        [1,4,3,2,5]
    ],
    [
        [5], 1, 1,
        [5]
    ]
]

run_functional_tests(Solution().reverseBetween, convert_test_params_to_lists(tests, [0, 3]))