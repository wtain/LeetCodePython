"""
https://leetcode.com/problems/even-odd-tree/

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.



Example 1:


Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
Example 2:


Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.
Example 3:


Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.


Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 106
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


# Runtime
# 543 ms
# Beats
# 66.88%
# Memory
# 140.1 MB
# Beats
# 14.93%
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        last_at_level = []

        def dfs(node: TreeNode, level: int) -> bool:
            if not node:
                return True

            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
            else:
                if node.val % 2 == 1:
                    return False

            inserted = False

            if level == len(last_at_level):
                last_at_level.append(node.val)
                inserted = True

            if not dfs(node.left, level + 1):
                return False

            if not inserted:
                if level % 2 == 0:
                    if last_at_level[level] >= node.val:
                        return False
                else:
                    if last_at_level[level] <= node.val:
                        return False
                last_at_level[level] = node.val

            if not dfs(node.right, level+1):
                return False
            return True

        return dfs(root, 0)


tests = [
    [build_tree_from_list([1,10,4,3,null,7,9,12,8,6,null,null,2]), True],
    [build_tree_from_list([5,4,2,3,3,7]), False],
    [build_tree_from_list([5,9,1,3,5,7]), False],
]

run_functional_tests(Solution().isEvenOddTree, tests)
