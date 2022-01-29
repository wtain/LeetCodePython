"""
https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
from typing import List

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 36 ms, faster than 52.52% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.9 MB, less than 43.41% of Python3 online submissions for Binary Tree Paths.
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def binaryTreePathsImpl(root: TreeNode, result: List[str], path: str):
            if root is None:
                return
            newpath: str = path
            if len(newpath) > 0:
                newpath += "->"
            newpath += str(root.val)
            if root.left is None and root.right is None:
                result.append(newpath)
            else:
                if root.left is not None:
                    binaryTreePathsImpl(root.left, result, newpath)
                if root.right is not None:
                    binaryTreePathsImpl(root.right, result, newpath)
        result: List[str] = []
        binaryTreePathsImpl(root, result, "")
        return result


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.right = TreeNode(5)
t1.right = TreeNode(3)

tests = [
    (t1, ['1->2->5', '1->3'])
]


run_functional_tests(Solution().binaryTreePaths, tests)

