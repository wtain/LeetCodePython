"""
https://leetcode.com/problems/root-equals-sum-of-children/

You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.



Example 1:


Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.
Example 2:


Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.


Constraints:

The tree consists only of the root, its left child, and its right child.
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 44 ms, faster than 37.04% of Python3 online submissions for Root Equals Sum of Children.
# Memory Usage: 13.9 MB, less than 45.60% of Python3 online submissions for Root Equals Sum of Children.
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val


tests = [
    [build_tree_from_list([10,4,6]), True],
    [build_tree_from_list([5,3,1]), False]
]

run_functional_tests(Solution().checkTree, tests)
