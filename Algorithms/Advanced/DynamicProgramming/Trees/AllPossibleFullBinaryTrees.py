"""
https://leetcode.com/problems/all-possible-full-binary-trees/

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.



Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]


Constraints:

1 <= n <= 20
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
from itertools import product
from typing import List

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params
from Common.TreeUtils import build_tree_from_list, build_tree_list_from_lists


# Runtime: 196 ms, faster than 69.65% of Python3 online submissions for All Possible Full Binary Trees.
# Memory Usage: 17.4 MB, less than 52.66% of Python3 online submissions for All Possible Full Binary Trees.
class Solution:

    @lru_cache
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(0)]

        if n % 2 == 0:
            return []

        result = []
        for i in range(1, n-1):
            subtrees1 = self.allPossibleFBT(i)
            subtrees2 = self.allPossibleFBT(n-1-i)
            for t1, t2 in product(subtrees1, subtrees2):
                root = TreeNode(0, t1, t2)
                result.append(root)

        return result


tests = [
    [7,
        [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    ],
    [3,
        [[0,0,0]]
    ]
]

run_functional_tests(Solution().allPossibleFBT, convert_test_params(tests, build_tree_list_from_lists, indexes=[1]))
