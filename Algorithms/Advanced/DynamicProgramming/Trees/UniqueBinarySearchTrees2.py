"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3961/
https://leetcode.com/problems/unique-binary-search-trees-ii/

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.



Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 8
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
from typing import List, Optional

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests, convert_test_params
from Common.TreeUtils import build_tree_from_list, build_tree_list_from_lists


# Runtime: 109 ms, faster than 5.04% of Python3 online submissions for Unique Binary Search Trees II.
# Memory Usage: 18.5 MB, less than 5.15% of Python3 online submissions for Unique Binary Search Trees II.
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []

        used = [False] * n

        def cloneTree(node: TreeNode) -> TreeNode:
            if not node:
                return None
            result = TreeNode(node.val)
            result.left = cloneTree(node.left)
            result.right = cloneTree(node.right)
            return result

        @lru_cache(None)
        def impl(vmin: int, vmax: int) -> List[TreeNode]:
            if vmin > vmax:
                return [None]
            result = []
            for i in range(n):
                v = i+1
                if used[i]:
                    continue
                if not (vmin <= v <= vmax):
                    continue

                used[i] = True
                node = TreeNode(v)

                rl = impl(vmin, v-1)
                rr = impl(v+1, vmax)
                for rli in rl:
                    node.left = rli
                    for rri in rr:
                        node.right = rri
                        result.append(cloneTree(node))

                used[i] = False
            if not result:
                result.append(None)
            return result

        return impl(1, n)


tests = [
    [3, [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]],
    [1, [[1]]]
]

run_functional_tests(Solution().generateTrees, convert_test_params(tests, build_tree_list_from_lists, indexes=[1]))