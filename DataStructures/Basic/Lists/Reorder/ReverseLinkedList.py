"""
https://leetcode.com/problems/reverse-linked-list/
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3966/
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from Common.Leetcode import ListNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists


# Runtime: 52 ms, faster than 24.51% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.3 MB, less than 62.20% of Python3 online submissions for Reverse Linked List.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev: ListNode = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


tests = [
    [
        [1],
        [1]
    ],
    [
        [],
        []
    ],
    [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
]

run_functional_tests(Solution().reverseList, convert_test_params_to_lists(tests))
