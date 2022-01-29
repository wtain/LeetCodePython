"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 52 ms, faster than 35.71% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.6 MB, less than 48.68% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left and root.right:
            dl = self.minDepth(root.left)
            dr = self.minDepth(root.right)
            return 1 + min(dl, dr)

        if root.left:
            return self.minDepth(root.left) + 1
        return self.minDepth(root.right) + 1
"""

"""
Runtime: 64 ms, faster than 18.93% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.4 MB, less than 66.48% of Python3 online submissions for Minimum Depth of Binary Tree.
"""

"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        dl = self.minDepth(root.left)
        dr = self.minDepth(root.right)

        if dl > 0 and dr > 0:
            return 1 + min(dl, dr)

        if dl > 0:
            return dl + 1
        return dr + 1
"""

"""
Runtime: 76 ms, faster than 10.73% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.6 MB, less than 53.25% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        dl = dr = 0

        if root.left:
            dl = self.minDepth(root.left)

        if root.right:
            dr = self.minDepth(root.right)

        if dl > 0 and dr > 0:
            return 1 + min(dl, dr)

        if dl > 0:
            return dl + 1
        return dr + 1


tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)

tests = [
    (tree1, 2),
    (tree2, 2)
]

run_functional_tests(Solution().minDepth, tests)