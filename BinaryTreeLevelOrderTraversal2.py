"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Runtime: 64 ms, faster than 11.41% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.3 MB, less than 25.48% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""
class Solution:

    def levelOrderBottomImpl(self, root: TreeNode, levels: List[List[int]], level: int):
        if root is None:
            return
        if level+1 > len(levels):
            levels.append([])
        levels[level].append(root.val)
        self.levelOrderBottomImpl(root.left, levels, level + 1)
        self.levelOrderBottomImpl(root.right, levels, level + 1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels: List[List[int]] = []
        self.levelOrderBottomImpl(root, levels, 0)
        return levels[::-1]


tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

"""
  [15,7],
  [9,20],
  [3]
"""
print(Solution().levelOrderBottom(tree1))

