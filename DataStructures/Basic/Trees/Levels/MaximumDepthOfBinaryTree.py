"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


"""
Runtime: 48 ms, faster than 37.70% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.3 MB, less than 64.04% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Runtime: 55 ms, faster than 50.62% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.4 MB, less than 77.69% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        level_count = 0
        level = [root]
        while level:
            next_level = []
            level_count += 1
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return level_count


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

tests = [
    (root, 3)
]

run_functional_tests(Solution().maxDepth, tests)
