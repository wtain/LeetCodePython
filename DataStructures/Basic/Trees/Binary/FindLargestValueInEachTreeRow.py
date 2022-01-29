"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).





Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 44 ms, faster than 87.92% of Python3 online submissions for Find Largest Value in Each Tree Row.
# Memory Usage: 17.1 MB, less than 13.76% of Python3 online submissions for Find Largest Value in Each Tree Row.
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def impl(node: TreeNode, level: int):
            nonlocal levels
            if not node:
                return
            if level < len(levels):
                levels[level] = max(levels[level], node.val)
            else:
                levels.append(node.val)
            impl(node.left, level + 1)
            impl(node.right, level + 1)

        impl(root, 0)
        return levels


tests = [
    [build_tree_from_list([1,3,2,5,3,null,9]), [1,3,9]],
    [build_tree_from_list([1,2,3]), [1,3]],
    [build_tree_from_list([1]), [1]],
    [build_tree_from_list([1,null,2]), [1,2]],
    [build_tree_from_list([]), []]
]

run_functional_tests(Solution().largestValues, tests)