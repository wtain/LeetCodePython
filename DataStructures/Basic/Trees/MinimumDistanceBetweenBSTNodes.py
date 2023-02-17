"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105


Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""
from typing import Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime
# 35 ms
# Beats
# 56.88%
# Memory
# 13.8 MB
# Beats
# 74.83%
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        mindist = float('inf')

        def impl(node: TreeNode, vmin, vmax) -> (int, int):
            nonlocal mindist
            if node.left:
                dist = node.val - node.left.val
                mindist = min(mindist, dist)
                mn1, mx1 = node.left.val, node.left.val
                min1, max1 = impl(node.left, mn1, mx1)
                dist = node.val - max1
                mindist = min(mindist, dist)
                vmin = min(vmin, min1)
            if node.right:
                dist = node.right.val - node.val
                mindist = min(mindist, dist)
                mn1, mx1 = node.right.val, node.right.val
                min1, max1 = impl(node.right, mn1, mx1)
                dist = min1 - node.val
                mindist = min(mindist, dist)
                vmax = max(vmax, max1)
            return vmin, vmax

        impl(root, root.val, root.val)
        return mindist


tests = [
    [build_tree_from_list([4,2,6,1,3]), 1],
    [build_tree_from_list([1,0,48,null,null,12,49]), 1],
]

run_functional_tests(Solution().minDiffInBST, tests)
