"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3733/
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Common.Leetcode import ListNode, TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists


# Runtime: 144 ms, faster than 15.99% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 20.6 MB, less than 15.16% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# class Solution:
#
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#
#         def findMiddle(head: ListNode, end: ListNode) -> ListNode:
#             current = head
#             if current == end:
#                 return current
#             current2 = current
#             while current2 != end:
#                 current2 = current2.next
#                 if current2 == end:
#                     break
#                 current = current.next
#                 current2 = current2.next
#             return current
#
#         def sortedListToBSTImpl(head: ListNode, end: ListNode) -> TreeNode:
#             if head == end:
#                 return None
#             middle = findMiddle(head, end)
#             return TreeNode(middle.val,
#                             sortedListToBSTImpl(head, middle),
#                             sortedListToBSTImpl(middle.next, end))
#
#         return sortedListToBSTImpl(head, None)


# Runtime: 132 ms, faster than 57.22% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 20.3 MB, less than 57.37% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
class Solution:

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def helper(beg: int, end: int) -> TreeNode:
            if beg > end:
                return None
            mid = beg + (end - beg) // 2
            left = helper(beg, mid - 1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = helper(mid + 1, end)
            return root

        self.head, copy, n = head, head, 0
        while copy:
            copy = copy.next
            n += 1

        return helper(0, n-1)


tests = [
    [
        [-10,-3,0,5,9],
        TreeNode(0,
                 TreeNode(-3,
                          TreeNode(-10)),
                 TreeNode(9,
                          TreeNode(5)))
    ],
    [
        [],
        None
    ],
    [
        [0],
        TreeNode(0)
    ],
    [
        [1,3],
        TreeNode(3,
                 TreeNode(1))
    ]
]

# todo: accept result if balanced
run_functional_tests(Solution().sortedListToBST, convert_test_params_to_lists(tests, [0]))