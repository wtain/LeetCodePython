"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-25

Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""
from typing import Optional, List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime
# 41
# ms
# Beats
# 15.76%
# Analyze Complexity
# Memory
# 16.54
# MB
# Beats
# 20.02%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        to_visit, visited = [], []
        if root:
            to_visit.append(root)
        while to_visit:
            p = to_visit.pop()
            visited.append(p.val)
            if p.left:
                to_visit.append(p.left)
            if p.right:
                to_visit.append(p.right)
        return list(reversed(visited))


tests = [
    [build_tree_from_list([1,null,2,3]), [3,2,1]],
    [build_tree_from_list([]), []],
]

run_functional_tests(Solution().postorderTraversal, tests)
