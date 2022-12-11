"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
from typing import Optional

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

# WRONG
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         maxSum = root.val
#
#         def impl(root, sumFromRoot, maxSumParents, path):
#             nonlocal maxSum
#             sumFromRoot += root.val
#             maxSumParents = max(maxSumParents, sumFromRoot)
#             maxSumInternal, sumInternal = sumFromRoot, sumFromRoot
#             for v in path:
#                 sumInternal -= v
#                 maxSumInternal = max(maxSumInternal, sumInternal)
#             maxSum = max(maxSum, maxSumInternal)
#             maxSum = max(maxSum, maxSumParents)
#
#             maxSumRootLeft, maxSumRootRight = sumFromRoot, sumFromRoot
#
#             if root.left:
#                 maxSumRootLeft = impl(root.left, sumFromRoot, maxSumRootLeft, path + [root.val])
#
#             if root.right:
#                 maxSumRootRight = impl(root.right, sumFromRoot, maxSumRootRight, path + [root.val])
#
#             maxSumParents = max(max(maxSumRootLeft, maxSumRootRight), maxSumParents)
#             maxSum = max(maxSum, maxSumParents)
#
#             sumCross = maxSumRootLeft - sumFromRoot + maxSumRootRight - sumFromRoot + root.val
#             maxSum = max(sumCross, sumCross)
#
#             return maxSumParents
#
#         impl(root, 0, maxSum, [])
#
#         return maxSum


# Runtime
# 261 ms
# Beats
# 5.68%
# Memory
# 21.3 MB
# Beats
# 63.68%
# https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/2827786/binary-tree-maximum-path-sum/
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        def impl(node):
            nonlocal max_path
            if not node:
                return 0
            left = max(impl(node.left), 0)
            right = max(impl(node.right), 0)
            max_path = max(max_path, left + right + node.val)
            return max(left + node.val, right + node.val)

        impl(root)
        return max_path


tests = [
    [build_tree_from_list([1,2,3]), 6],
    [build_tree_from_list([-10,9,20,null,null,15,7]), 42]
]

run_functional_tests(Solution().maxPathSum, tests)
