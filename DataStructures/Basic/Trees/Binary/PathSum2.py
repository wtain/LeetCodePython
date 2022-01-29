"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3838/
https://leetcode.com/problems/path-sum-ii/

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 44 ms, faster than 77.11% of Python3 online submissions for Path Sum II.
# Memory Usage: 15.7 MB, less than 65.10% of Python3 online submissions for Path Sum II.
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []

        def impl(node: TreeNode, s: int, path: List[int]):
            nonlocal result
            if not node:
                return
            ns = s - node.val
            path.append(node.val)
            if not node.left and not node.right:
                if ns == 0:
                    result.append(path.copy())
            else:
                impl(node.left, ns, path)
                impl(node.right, ns, path)
            path.pop()

        impl(root, targetSum, [])
        return result


tests = [
    [
        TreeNode(5,
                 TreeNode(4,
                          TreeNode(11,
                                   TreeNode(7),
                                   TreeNode(2))),
                 TreeNode(8,
                          TreeNode(13),
                          TreeNode(4,
                                   TreeNode(5),
                                   TreeNode(1)))),
        22,
        [[5,4,11,2],[5,8,4,5]]
    ],
    [
        TreeNode(1,
                 TreeNode(2),
                 TreeNode(3)),
        5,
        []
    ],
    [
        TreeNode(1,
                 TreeNode(2)),
        0,
        []
    ]
]

run_functional_tests(Solution().pathSum, tests)