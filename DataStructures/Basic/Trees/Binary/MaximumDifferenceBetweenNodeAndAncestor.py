"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.



Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3


Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 57 ms, faster than 17.83% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 20.6 MB, less than 44.74% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def impl(node: TreeNode, a: int, b: int) -> int:
            if not node:
                return 0

            dl = impl(node.left, min(a, node.val), max(b, node.val))
            dr = impl(node.right, min(a, node.val), max(b, node.val))
            d = max(abs(a-node.val), abs(b-node.val))
            d = max(d, dl, dr)
            return d

        return impl(root, root.val, root.val)


tests = [
    [build_tree_from_list([8,3,10,1,6,null,14,null,null,4,7,13]), 7],
    [build_tree_from_list([1,null,2,null,0,3]), 3]
]

run_functional_tests(Solution().maxAncestorDiff, tests)
