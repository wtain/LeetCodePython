"""
https://leetcode.com/problems/path-sum-iii/

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).



Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
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


# Runtime: 184 ms, faster than 47.57% of Python3 online submissions for Path Sum III.
# Memory Usage: 15.4 MB, less than 63.48% of Python3 online submissions for Path Sum III.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result, path = 0, []

        def impl(root: TreeNode):
            nonlocal result, path, targetSum
            if not root:
                return
            part_sum = path[-1] if path else 0
            part_sum += root.val
            for ps in path:
                pps = part_sum - ps
                if pps == targetSum:
                    result += 1
            path.append(part_sum)
            if part_sum == targetSum:
                result += 1
            impl(root.left)
            impl(root.right)
            path.pop()

        impl(root)

        return result


tests = [
    [
        build_tree_from_list([10,5,-3,3,2,null,11,3,-2,null,1]), 8, 3
    ],
    [
        build_tree_from_list([5,4,8,11,null,13,4,7,2,null,null,5,1]), 22, 3
    ]
]

run_functional_tests(Solution().pathSum, tests)