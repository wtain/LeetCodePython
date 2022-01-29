"""
https://leetcode.com/problems/add-two-numbers/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3601/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Runtime: 72 ms, faster than 51.91% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.2 MB, less than 66.48% of Python3 online submissions for Add Two Numbers.
from Common.DataTypes.Leetcode import ListNode
from Common.ListUtils import buildNumberAsList
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        result = ListNode(-1)
        curr = result
        while l1 or l2 or c:
            v = c
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            c = v // 10
            v = v % 10
            curr.next = ListNode(v)
            curr = curr.next
        return result.next


tests = [
    [[2,4,3], [5,6,4], [7,0,8]],
    [[0], [0], [0]],
    [[9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]]
]

run_functional_tests(Solution().addTwoNumbers, convert_test_params(tests, buildNumberAsList))
