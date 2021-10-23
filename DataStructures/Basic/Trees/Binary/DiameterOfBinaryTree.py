"""
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 51 ms, faster than 36.98% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.3 MB, less than 52.00% of Python3 online submissions for Diameter of Binary Tree.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_dist = 0

        def impl(node: TreeNode) -> int:
            nonlocal max_dist
            if not node:
                return 0
            current_max1 = impl(node.left)
            current_max2 = impl(node.right)
            curr_max = max(current_max1, current_max2) + 1
            dist = current_max1 + current_max2
            max_dist = max(max_dist, dist)
            return curr_max

        impl(root)
        return max_dist


tests = [
    [
        build_tree_from_list([1,2,3,4,5]), 3
    ],
    [
        build_tree_from_list([1,2]), 1
    ]
]

run_functional_tests(Solution().diameterOfBinaryTree, tests)