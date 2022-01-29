"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3712/
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Common.DataTypes.Leetcode import ListNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists


# Runtime: 36 ms, faster than 43.82% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 14.2 MB, less than 77.52% of Python3 online submissions for Remove Nth Node From End of List.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = None
        current = head
        current2 = head
        for _ in range(n):
            current2 = current2.next

        while current2:
            current2 = current2.next
            prev = current
            current = current.next

        if not prev:
            return head.next

        prev.next = prev.next.next

        return head


tests = [
    [
        [1,2,3,4,5],
        2,
        [1,2,3,5]
    ],
    [
        [1],
        1,
        []
    ],
    [
        [1, 2],
        1,
        [1]
    ],
    [
        [1, 2],
        2,
        [2]
    ]
]

run_functional_tests(Solution().removeNthFromEnd, convert_test_params_to_lists(tests, [0, 2]))