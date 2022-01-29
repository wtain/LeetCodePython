"""
https://leetcode.com/problems/linked-list-in-binary-tree/

Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.



Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.


Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
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
from typing import Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import ListNode, TreeNode
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 144 ms, faster than 30.88% of Python3 online submissions for Linked List in Binary Tree.
# Memory Usage: 17.5 MB, less than 11.90% of Python3 online submissions for Linked List in Binary Tree.
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def compare(list_node: ListNode, tree_node: TreeNode) -> bool:
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val != tree_node.val:
                return False
            return compare(list_node.next, tree_node.left) or compare(list_node.next, tree_node.right)

        if compare(head, root):
            return True
        return root and (self.isSubPath(head, root.left) or self.isSubPath(head, root.right))


tests = [
    [build_list([4,2,8]), build_tree_from_list([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]), True],
    [build_list([1,4,2,6]), build_tree_from_list([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]), True],
    [build_list([1,4,2,6,8]), build_tree_from_list([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]), False]
]

run_functional_tests(Solution().isSubPath, tests)
