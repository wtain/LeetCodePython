"""
https://leetcode.com/problems/leaf-similar-trees/description/

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""
from typing import Optional, List

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
# 27 ms
# Beats
# 98.52%
# Memory
# 14 MB
# Beats
# 46.25%
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaves(root: TreeNode) -> List[int]:
            result = []

            def impl(root: TreeNode):
                if not root:
                    return
                if not root.left and not root.right:
                    result.append(root.val)
                    return
                impl(root.left)
                impl(root.right)

            impl(root)
            return result

        return get_leaves(root1) == get_leaves(root2)


tests = [
    [
        build_tree_from_list([3,5,1,6,2,9,8,null,null,7,4]),
        build_tree_from_list([3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]),
        True
    ],
    [
        build_tree_from_list([1,2,3]),
        build_tree_from_list([1,3,2]),
        False
    ]
]

run_functional_tests(Solution().leafSimilar, tests)
