"""
https://leetcode.com/problems/construct-string-from-binary-tree/

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.



Example 1:


Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:


Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
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


# Runtime: 56 ms, faster than 89.12% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 16.5 MB, less than 30.02% of Python3 online submissions for Construct String from Binary Tree.
# https://leetcode.com/submissions/detail/336347637/
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""

        def impl(node: TreeNode):
            nonlocal result
            if not node:
                return

            result += str(node.val)

            if node.left or node.right:
                result += "("
                impl(node.left)
                result += ")"

            if node.right:
                result += "("
                impl(node.right)
                result += ")"

        impl(root)

        return result


tests = [
    [build_tree_from_list([1,2,3,4]), "1(2(4))(3)"],
    [build_tree_from_list([1,2,3,null,4]), "1(2()(4))(3)"]
]

run_functional_tests(Solution().tree2str, tests)
