"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/description/?envType=daily-question&envId=2023-11-01

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""
from typing import Optional, List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime
# Details
# 52ms
# Beats 77.73%of users with Python3
# Memory
# Details
# 20.29MB
# Beats 86.51%of users with Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = curr_len = max_len = 0

        def impl(node):
            nonlocal current, curr_len, max_len, result
            if not node:
                return
            impl(node.left)
            if curr_len == 0:
                max_len = curr_len = 1
                current = node.val
                result.append(current)
            elif node.val == current:
                curr_len += 1
                if curr_len == max_len:
                    result.append(current)
                elif curr_len > max_len:
                    max_len = curr_len
                    result = [current]
            else:
                curr_len = 1
                current = node.val
                if curr_len == max_len:
                    result.append(current)
            impl(node.right)

        impl(root)

        return result


tests = [
    [build_tree_from_list([1,null,2,2]), [2]],
    [build_tree_from_list([0]), [0]],
]

run_functional_tests(Solution().findMode, tests)
