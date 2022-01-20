"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.



Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 185 ms, faster than 22.30% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.7 MB, less than 59.81% of Python3 online submissions for Insert into a Binary Search Tree.
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)
#         if val > root.val:
#             if not root.right:
#                 root.right = TreeNode(val)
#             else:
#                 self.insertIntoBST(root.right, val)
#         else:
#             if not root.left:
#                 root.left = TreeNode(val)
#             else:
#                 self.insertIntoBST(root.left, val)
#         return root


# Runtime: 128 ms, faster than 94.66% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.9 MB, less than 26.36% of Python3 online submissions for Insert into a Binary Search Tree.
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node
        node, parent = root, None
        while node:
            if val > node.val:
                node, parent = node.right, node
                if not node:
                    parent.right = new_node
            else:
                node, parent = node.left, node
                if not node:
                    parent.left = new_node
        return root


tests = [
    [build_tree_from_list([]), 5, build_tree_from_list([5])],
    [build_tree_from_list([4,2,7,1,3]), 5, build_tree_from_list([4,2,7,1,3,5])],
    [build_tree_from_list([40,20,60,10,30,50,70]), 25, build_tree_from_list([40,20,60,10,30,50,70,null,null,25])],
    [build_tree_from_list([4,2,7,1,3,null,null,null,null,null,null]), 5, build_tree_from_list([4,2,7,1,3,5])]
]

run_functional_tests(Solution().insertIntoBST, tests)

