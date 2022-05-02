"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.



Example 1:


Input: root = [0,1,2,3,4,3,4]
Output: "dba"
Example 2:


Input: root = [25,1,3,1,3,0,2]
Output: "adz"
Example 3:


Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"


Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
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


# Runtime: 92 ms, faster than 12.25% of Python3 online submissions for Smallest String Starting From Leaf.
# Memory Usage: 15.4 MB, less than 97.40% of Python3 online submissions for Smallest String Starting From Leaf.
# class Solution:
#     def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
#
#         smallest = None
#
#         def impl(node: TreeNode, suffix: str):
#             nonlocal smallest
#             if not node:
#                 return
#             res = chr(ord('a') + node.val) + suffix
#             if not node.left and not node.right:
#                 smallest = min(smallest or res, res)
#             impl(node.left, res)
#             impl(node.right, res)
#
#         impl(root, "")
#         return smallest


# Runtime: 75 ms, faster than 32.10% of Python3 online submissions for Smallest String Starting From Leaf.
# Memory Usage: 15.5 MB, less than 37.48% of Python3 online submissions for Smallest String Starting From Leaf.
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        smallest = None

        def get_depth(node: TreeNode) -> int:
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        max_depth = get_depth(root)

        def impl(node: TreeNode, suffix_code: int, power: int, depth: int):
            nonlocal smallest, max_depth
            if not node:
                return
            res = power*(node.val+1) + suffix_code
            if not node.left and not node.right:
                if max_depth-depth-1 > 0:
                    res *= 27 ** (max_depth-depth-1)
                smallest = min(smallest or res, res)
            power1 = 27 * power
            impl(node.left, res, power1, depth+1)
            impl(node.right, res, power1, depth+1)

        def decode(code: int) -> str:
            result = ""
            while code:
                d = chr(ord('a') + code % 27 - 1)
                if 'a' <= d <= 'z':
                    result += d
                code //= 27
            return result[::-1]

        impl(root, 0, 1, 0)
        return decode(smallest)


tests = [
    [
        build_tree_from_list([0,1,2,3,4,3,4]), "dba"
    ],
    [
        build_tree_from_list([25,1,3,1,3,0,2]), "adz"
    ],
    [
        build_tree_from_list([2,2,1,null,1,0,null,0]), "abc"
    ],
    [
        build_tree_from_list([3,9,20,null,null,15,7]), "hud"
    ]
]

run_functional_tests(Solution().smallestFromLeaf, tests)
