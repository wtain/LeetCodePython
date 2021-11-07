"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.



Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 276 ms, faster than 97.35% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 18.9 MB, less than 8.14% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = []
        smallest, current_level, result = 0, 0, 1
        if root:
            level.append(root)
            smallest = root.val
        while level:
            current_level += 1
            next_level, s = [], 0
            for n in level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
                s += n.val
            if s > smallest:
                smallest = s
                result = current_level
            level = next_level
        return result


tests = [
    [build_tree_from_list([1,7,0,7,-8,null,null]), 2],
    [build_tree_from_list([989,null,10250,98693,-89388,null,null,null,-32127]), 2],

    [build_tree_from_list([-100,-200,-300,-20,-5,-10,null]), 3],
    [build_tree_from_list([1]), 1]
]

run_functional_tests(Solution().maxLevelSum, tests)
