"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3749/
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 80.06% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 15.2 MB, less than 12.67% of Python3 online submissions for Binary Tree Level Order Traversal.
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []

        def traverse(root: TreeNode, level: int):
            nonlocal levels
            if not root:
                return
            if level >= len(levels):
                levels.append([])
            levels[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 0)

        return levels


tests = [
    [
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5)),
                 TreeNode(3)),
        [[1],[2,3],[4,5]]
    ],
    [
        TreeNode(3,
                 TreeNode(9),
                 TreeNode(20,
                          TreeNode(15),
                          TreeNode(7))),
        [[3],[9,20],[15,7]]
    ],
    [
        TreeNode(1),
        [[1]]
    ],
    [
        null,
        []
    ]
]

run_functional_tests(Solution().levelOrder, tests)