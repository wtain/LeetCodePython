"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.ListUtils import build_list, build_list_with_loop
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 87.62% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.3 MB, less than 23.99% of Python3 online submissions for Linked List Cycle II.
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        if not fast:
            return None
        slow, fast = slow.next, fast.next
        if not fast:
            return None
        fast = fast.next
        while fast and id(slow) != id(fast):
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
        if id(slow) != id(fast):
            return None
        fast = head
        while id(slow) != id(fast):
            slow = slow.next
            fast = fast.next
        return slow


# Input: head = [3,2,0,-4], pos = 1
list1 = build_list([3,2,0,-4])
list1.next.next.next = list1.next

# head = [1,2], pos = 0
list2 = build_list([1, 2])
list2.next.next = list2

# Input: head = [1], pos = -1
list3 = build_list([1])


# todo: support
# todo: list with loop metric
# todo: print list with loop
# todo: customprint?

# tests = [
#     [list1, list1.next],
#     [list2, list2],
#     [list3, None],
# ]

tests = [
    [build_list_with_loop([3,2,0,-4], 1), 2],
    [build_list_with_loop([1,2], 0), 1],
    [build_list_with_loop([1], -1), None],
]


def customCheck(test, result) -> bool:
    if test[-1] is None:
        return not result
    return test[-1] == result.val


# , custom_tostring=lambda v: v if v is int else (str(v.val) if v else "(null)")
run_functional_tests(Solution().detectCycle, tests, custom_check=customCheck)
