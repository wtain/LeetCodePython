"""
https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.



Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 78 ms, faster than 86.45% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.6 MB, less than 28.83% of Python3 online submissions for Search in a Binary Search Tree.
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while current:
            if current.val == val:
                return current
            if current.val > val:
                current = current.left
            else:
                current = current.right
        return None


tests = [
    [build_tree_from_list([4,2,7,1,3]), 2, build_tree_from_list([2,1,3])],
    [build_tree_from_list([4,2,7,1,3]), 5, build_tree_from_list([])]
]

run_functional_tests(Solution().searchBST, tests)
