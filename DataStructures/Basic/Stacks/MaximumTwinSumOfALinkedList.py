"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.



Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.


Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Runtime
# 1032 ms
# Beats
# 14.49%
# Memory
# 56.9 MB
# Beats
# 13.9%
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         st = []
#         node = head
#         while node:
#             st.append(node.val)
#             node = node.next
#         result = 0
#         n = len(st)
#         node = head
#         for i in range(n//2):
#             v = node.val + st.pop()
#             result = max(result, v)
#             node = node.next
#         return result


# Runtime
# 911 ms
# Beats
# 57.30%
# Memory
# 56.7 MB
# Beats
# 19.47%
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         st = []
#         node = head
#         while node:
#             st.append(node.val)
#             node = node.next
#         result = 0
#         n = len(st)
#         for i in range(n//2):
#             v = st[i] + st[n-1-i]
#             result = max(result, v)
#         return result


# Runtime
# 787 ms
# Beats
# 92.44%
# Memory
# 38 MB
# Beats
# 86.79%
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next

            nx = slow.next
            slow.next = prev
            prev = slow
            slow = nx

        node1, node2 = prev, slow
        result = 0
        while node1:
            result = max(result, node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next
        return result


tests = [
    [build_list([5,4,2,1]), 6],
    [build_list([4,2,2,3]), 7],
    [build_list([1,100000]), 100001],
]

run_functional_tests(Solution().pairSum, tests)
