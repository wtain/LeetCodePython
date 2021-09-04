"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3745/
https://leetcode.com/problems/binary-tree-cameras/

Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.



Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minCameraCover(self, root: TreeNode) -> int:
#
#         def minCameraCoverImpl(root: TreeNode, prevCovered: bool, isroot: bool) -> int:
#             if not root:
#                 return 0
#
#             if isroot:
#                 return min(minCameraCoverImpl(root.left, False, False) + minCameraCoverImpl(root.right, False, False), 1 + minCameraCoverImpl(root.left, True, False) + minCameraCoverImpl(root.right, True, False))
#
#             if prevCovered:
#                 return minCameraCoverImpl(root.left, False, False) + minCameraCoverImpl(root.right, False, False)
#             else:
#                 return 1 + minCameraCoverImpl(root.left, True, False) + minCameraCoverImpl(root.right, True, False)
#
#         return minCameraCoverImpl(root, True, True)

# Three State Method

# Runtime: 56 ms, faster than 14.25% of Python3 online submissions for Binary Tree Cameras.
# Memory Usage: 14.5 MB, less than 91.40% of Python3 online submissions for Binary Tree Cameras.
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def solve(root: TreeNode) -> List[int]:
            if not root:
                return [0, 0, float('inf')]
            L = solve(root.left)
            R = solve(root.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L[:]) + min(R[:])

            return [dp0, dp1, dp2]

        return min(solve(root)[1:])


tests = [
    [
        TreeNode(0,
                 TreeNode(0,
                          TreeNode(0),
                          TreeNode(0))),
        1
    ],
    [
        TreeNode(0,
                 TreeNode(0,
                          TreeNode(0,
                                   TreeNode(0,
                                            null,
                                            TreeNode(0))))),
        2
    ],
    [
        TreeNode(0),
        1
    ]
]

run_functional_tests(Solution().minCameraCover, tests)