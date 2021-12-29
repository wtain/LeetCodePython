"""
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Common.Leetcode import ListNode
from Common.ObjectTestingUtils import run_functional_tests, convert_test_params_to_lists


# Runtime: 32 ms, faster than 60.47% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 14.3 MB, less than 11.11% of Python3 online submissions for Middle of the Linked List.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first, second = head, head
        while second:
            second = second.next
            if not second:
                return first
            second = second.next
            first = first.next
        return first


tests = [
    [[1,2,3,4,5], [3,4,5]],
    [[1,2,3,4,5,6], [4,5,6]]
]

run_functional_tests(Solution().middleNode, convert_test_params_to_lists(tests))
