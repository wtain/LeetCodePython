"""
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.



Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""
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
# 113 ms
# Beats
# 56.12%
# Memory
# 17.7 MB
# Beats
# 56.53%
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0

        def dfs(node: TreeNode, even_parent: bool, even_grandparent):
            nonlocal result
            if not node:
                return
            if even_grandparent:
                result += node.val
            dfs(node.left, node.val % 2 == 0, even_parent)
            dfs(node.right, node.val % 2 == 0, even_parent)

        dfs(root, False, False)

        return result


tests = [
    [build_tree_from_list([6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]), 18],
    [build_tree_from_list([1]), 0],
]

run_functional_tests(Solution().sumEvenGrandparent, tests)
