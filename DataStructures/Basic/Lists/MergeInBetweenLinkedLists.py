"""
https://leetcode.com/problems/merge-in-between-linked-lists/description/?envType=daily-question&envId=2024-03-20

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.



Example 1:


Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.


Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
"""
from Common.DataTypes.Leetcode import ListNode
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 187
# ms
# Beats
# 78.81%
# of users with Python3
# Memory
# 21.10
# MB
# Beats
# 31.60%
# of users with Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#
#         def advance(node, n):
#             while n:
#                 n -= 1
#                 node = node.next
#             return node
#
#         def find_last(node):
#             while node and node.next:
#                 node = node.next
#             return node
#
#         p1 = advance(list1, a-1)
#         p2 = advance(list1, b+1)
#
#         p1.next = list2
#         p3 = find_last(list2)
#
#         p3.next = p2
#
#         return list1

# Runtime
# 193
# ms
# Beats
# 54.04%
# of users with Python3
# Memory
# 21.00
# MB
# Beats
# 87.43%
# of users with Python3
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        def advance(node, n):
            while n:
                n -= 1
                node = node.next
            return node

        def find_last(node):
            while node and node.next:
                node = node.next
            return node

        p1 = advance(list1, a-1)
        p2 = advance(p1, b+1-a+1)

        p1.next = list2
        p3 = find_last(list2)

        p3.next = p2

        return list1


tests = [
    [build_list([10,1,13,6,9,5]), 3, 4, build_list([1000000,1000001,1000002]), build_list([10,1,13,1000000,1000001,1000002,5])],
    [build_list([0,1,2,3,4,5,6]), 2, 5, build_list([1000000,1000001,1000002,1000003,1000004]), build_list([0,1,1000000,1000001,1000002,1000003,1000004,6])],
]

run_functional_tests(Solution().mergeInBetween, tests)
