"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from typing import Optional, List

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
# 36 ms
# Beats
# 58.29%
# Memory
# 14.2 MB
# Beats
# 48.21%
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        to_visit = []
        if root:
            to_visit.append(root)
        while to_visit:
            result.append([])
            next_level = []
            is_odd = len(result) % 2 == 0
            for node in reversed(to_visit):
                result[-1].append(node.val)
                if node.right and is_odd:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
                if node.right and not is_odd:
                    next_level.append(node.right)
            to_visit = next_level
        return result


tests = [
    [build_tree_from_list([3,9,20,null,null,15,7]), [[3],[20,9],[15,7]]],
    [build_tree_from_list([1]), [[1]]],
    [build_tree_from_list([]), []],
]

run_functional_tests(Solution().zigzagLevelOrder, tests)
