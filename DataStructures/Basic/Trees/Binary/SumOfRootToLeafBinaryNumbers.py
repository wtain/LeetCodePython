"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.



Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 50 ms, faster than 26.50% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 14.7 MB, less than 39.83% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        result = 0

        def impl(node: TreeNode, current):
            nonlocal result
            if not node:
                return
            current += node.val
            if not node.left and not node.right:
                result += current
            else:
                current *= 2
                impl(node.left, current)
                impl(node.right, current)

        impl(root, 0)

        return result


tests = [
    [build_tree_from_list([1,0,1,0,1,0,1]), 22],
    [build_tree_from_list([0]), 0]
]

run_functional_tests(Solution().sumRootToLeaf, tests)
