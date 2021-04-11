"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3704/
https://leetcode.com/problems/deepest-leaves-sum/

Given the root of a binary tree, return the sum of values of its deepest leaves.


Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 84 ms, faster than 93.94% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 17.8 MB, less than 40.88% of Python3 online submissions for Deepest Leaves Sum.
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        current_sum = 0
        max_depth = 0

        def deepest_sum_impl(node: TreeNode, depth: int):
            nonlocal current_sum, max_depth
            if not node:
                return
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    current_sum = node.val
                elif depth == max_depth:
                    current_sum += node.val
            else:
                deepest_sum_impl(node.left, depth + 1)
                deepest_sum_impl(node.right, depth + 1)

        deepest_sum_impl(root, 0)

        return current_sum


tests = [
    (
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(4,
                                   TreeNode(7)),
                          TreeNode(5)),
                 TreeNode(3,
                          None,
                          TreeNode(6,
                                   None,
                                   TreeNode(8)))),
        15
    ),
    (
        TreeNode(6,
                 TreeNode(7,
                          TreeNode(2,
                                   TreeNode(9)),
                          TreeNode(7,
                                   TreeNode(1),
                                   TreeNode(4))),
                 TreeNode(8,
                          TreeNode(1),
                          TreeNode(3,
                                   None,
                                   TreeNode(5)))),
        19
    )
]

run_functional_tests(Solution().deepestLeavesSum, tests)
