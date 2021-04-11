"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""

from typing import List


# Runtime: 32 ms, faster than 64.91% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 14 MB, less than 89.96% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
from Common.Leetcode import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result = (result << 1) + head.val
            head = head.next
        return result


def buildList(vals: List[int]) -> ListNode:
    head = ListNode()
    prev = head
    for v in vals:
        prev.next = ListNode(v)
        prev = prev.next
    return head.next


tests = [
    (buildList([1,0,1]), 5),
    (buildList([0]), 0),
    (buildList([1]), 1),
    (buildList([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]), 18880),
    (buildList([0,0]), 0)
]

for test in tests:
    result = Solution().getDecimalValue(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))