"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
"""


# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Runtime: 1128 ms, faster than 57.65% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.8 MB, less than 62.89% of Python3 online submissions for Swapping Nodes in a Linked List.
from Common.DataTypes.Leetcode import ListNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists


# Runtime: 1172 ms, faster than 74.86% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.5 MB, less than 53.33% of Python3 online submissions for Swapping Nodes in a Linked List.
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        def list_len(h: ListNode) -> int:
            n = 0
            while h:
                n += 1
                h = h.next
            return n

        def get_node(h: ListNode, i: int) -> ListNode:
            i -= 1
            while i > 0 and h:
                i -= 1
                h = h.next
            return h

        n = list_len(head)
        n1 = get_node(head, k)
        n2 = get_node(head, n+1-k)
        n1.val, n2.val = n2.val, n1.val

        return head


tests = [
    [[1,2,3,4,5], 2, [1,4,3,2,5]],
    [[7,9,6,6,7,8,3,0,9,5], 5, [7,9,6,6,8,7,3,0,9,5]],
    [[1], 1, [1]],
    [[1,2], 1, [2,1]],
    [[1,2,3], 2, [1,2,3]]
]

run_functional_tests(Solution().swapNodes, convert_test_params_to_lists(tests, [0, 2]))
