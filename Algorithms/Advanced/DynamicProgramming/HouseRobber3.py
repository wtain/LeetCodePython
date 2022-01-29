"""
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.



Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#
#         def impl(root: TreeNode, can_rob: bool) -> int:
#             if not root:
#                 return 0
#             result = impl(root.left, True) + impl(root.right, True)
#             if can_rob:
#                 result = max(result, root.val + impl(root.left, False) + impl(root.right, False))
#             return result
#
#         return impl(root, True)


# Runtime: 5132 ms, faster than 5.33% of Python3 online submissions for House Robber III.
# Memory Usage: 16.1 MB, less than 94.67% of Python3 online submissions for House Robber III.
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#
#         @lru_cache
#         def impl(root: TreeNode, can_rob: bool) -> int:
#             if not root:
#                 return 0
#             result = impl(root.left, True) + impl(root.right, True)
#             if can_rob:
#                 result = max(result, root.val + impl(root.left, False) + impl(root.right, False))
#             return result
#
#         return impl(root, True)


# Runtime: 56 ms, faster than 39.51% of Python3 online submissions for House Robber III.
# Memory Usage: 18.6 MB, less than 8.74% of Python3 online submissions for House Robber III.
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#
#         @lru_cache(None)
#         def impl(root: TreeNode, can_rob: bool) -> int:
#             if not root:
#                 return 0
#             result = impl(root.left, True) + impl(root.right, True)
#             if can_rob:
#                 result = max(result, root.val + impl(root.left, False) + impl(root.right, False))
#             return result
#
#         return impl(root, True)

# Runtime: 48 ms, faster than 78.02% of Python3 online submissions for House Robber III.
# Memory Usage: 16.3 MB, less than 56.48% of Python3 online submissions for House Robber III.
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#
#         def impl(root: TreeNode) -> (int, int):
#             if not root:
#                 return 0, 0
#             l_rob, l_leave = impl(root.left)
#             r_rob, r_leave = impl(root.right)
#             return root.val + l_leave + r_leave, max(l_rob, l_leave) + max(r_rob, r_leave)
#
#         return max(impl(root))


# Runtime: 36 ms, faster than 99.45% of Python3 online submissions for House Robber III.
# Memory Usage: 17.9 MB, less than 13.74% of Python3 online submissions for House Robber III.
class Solution:
    def rob(self, root: TreeNode) -> int:

        @lru_cache(None)
        def impl(root: TreeNode) -> (int, int):
            if not root:
                return 0, 0
            l_rob, l_leave = impl(root.left)
            r_rob, r_leave = impl(root.right)
            return root.val + l_leave + r_leave, max(l_rob, l_leave) + max(r_rob, r_leave)

        return max(impl(root))


tests = [
    [
        TreeNode(3,
                 TreeNode(2,
                          null,
                          TreeNode(3)),
                 TreeNode(3,
                          null,
                          TreeNode(1))),
        7
    ],
    [
        TreeNode(3,
                 TreeNode(4,
                          TreeNode(1),
                          TreeNode(3)),
                 TreeNode(5,
                          null,
                          TreeNode(1))),
        9
    ]
]

run_functional_tests(Solution().rob, tests)