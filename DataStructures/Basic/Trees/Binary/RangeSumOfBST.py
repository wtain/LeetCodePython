"""
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].



Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.


Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
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


# Runtime: 212 ms, faster than 63.88% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.3 MB, less than 59.19% of Python3 online submissions for Range Sum of BST.
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        to_visit = []
        if root:
            to_visit.append((root, low, high))
        while to_visit:
            node, l, r = to_visit.pop()

            if node.val < l:
                if node.right:
                    to_visit.append((node.right, l, r))
            elif node.val > r:
                if node.left:
                    to_visit.append((node.left, l, r))
            else:
                result += node.val
                if node.left:
                    to_visit.append((node.left, l, node.val))
                if node.right:
                    to_visit.append((node.right, node.val, r))
        return result


tests = [
    [build_tree_from_list([15,9,21,7,13,19,23,5,null,11,null,17]), 19, 21, 40],
    [build_tree_from_list([10,5,15,3,7,null,18]), 7, 15, 32],
    [build_tree_from_list([10,5,15,3,7,13,18,1,null,6]), 6, 10, 23]
]

run_functional_tests(Solution().rangeSumBST, tests)
