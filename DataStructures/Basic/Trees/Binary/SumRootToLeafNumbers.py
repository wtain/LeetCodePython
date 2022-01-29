"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.



Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
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


# Runtime: 28 ms, faster than 89.40% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 14.4 MB, less than 18.39% of Python3 online submissions for Sum Root to Leaf Numbers.
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def impl(node: TreeNode, v: int):
            nonlocal result
            v1 = v + node.val
            if not node.left and not node.right:
                result += v1
                return
            v2 = 10 * v1
            if node.left:
                impl(node.left, v2)
            if node.right:
                impl(node.right, v2)

        if root:
            impl(root, 0)

        return result


tests = [
    [build_tree_from_list([1,2,3]), 25],
    [build_tree_from_list([4,9,0,5,1]), 1026]
]

run_functional_tests(Solution().sumNumbers, tests)
