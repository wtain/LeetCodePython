"""
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


Follow up: Could you solve it without reversing the input lists?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List

from Common.Leetcode import ListNode
from Common.ListUtils import buildNumberAsList
from Common.ObjectTestingUtils import run_functional_tests, convert_test_params


# Runtime: 85 ms, faster than 18.95% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.4 MB, less than 13.49% of Python3 online submissions for Add Two Numbers II.
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#
#         def to_stack(l: ListNode) -> List[int]:
#             s = []
#             while l:
#                 s.append(l.val)
#                 l = l.next
#             return s
#
#         s1, s2 = to_stack(l1), to_stack(l2)
#         result = None
#         carry = 0
#         while s1 or s2 or carry:
#             v1 = s1.pop() if s1 else 0
#             v2 = s2.pop() if s2 else 0
#             v = v1 + v2 + carry
#             carry = v // 10
#             v %= 10
#             node = ListNode(v)
#             node.next = result
#             result = node
#         return result


# Runtime: 76 ms, faster than 50.22% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.4 MB, less than 13.42% of Python3 online submissions for Add Two Numbers II.
# https://leetcode.com/problems/add-two-numbers-ii/discuss/1373905/Use-2ms-without-stack-and-reverse-in-Java
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        d1 = ListNode(-1, l1)
        d2 = ListNode(-1, l2)
        f1 = s1 = d1
        f2 = s2 = d2
        while f1 and f2:
            f1 = f1.next
            f2 = f2.next
        curr_result = result = ListNode(0)

        while s1.next and s2.next:
            v1 = v2 = 0
            if not f2:
                s1 = s1.next
                v1 = s1.val
            else:
                f2 = f2.next
            if not f1:
                s2 = s2.next
                v2 = s2.val
            else:
                f1 = f1.next
            curr_result.next = ListNode(v1 + v2)
            curr_result = curr_result.next

        s, f = result, result.next
        while f:
            if f.val >= 10:
                f.val %= 10
                while s != f:
                    s.val += 1
                    if s.val >= 10:
                        s.val %= 10
                    s = s.next
            if f.val != 9:
                while s != f:
                    s = s.next
            f = f.next

        if result.val == 1:
            return result
        return result.next


tests = [
    [[7,2,4,3], [5,6,4], [7,8,0,7]],
    [[2,4,3], [5,6,4], [8,0,7]],
    [[0], [0], [0]]
]

run_functional_tests(Solution().addTwoNumbers, convert_test_params(tests, buildNumberAsList))