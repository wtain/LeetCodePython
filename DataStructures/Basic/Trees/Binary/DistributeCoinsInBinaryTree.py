"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/description/?envType=daily-question&envId=2024-05-18

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.



Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.


Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
"""
from typing import Optional

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# untime
# 40
# ms
# Beats
# 44.99%
# of users with Python3
# Memory
# 16.55
# MB
# Beats
# 38.65%
# of users with Python3
# https://leetcode.com/problems/distribute-coins-in-binary-tree/editorial/?envType=daily-question&envId=2024-05-18
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(curr):
            nonlocal result
            if not curr:
                return 0

            left_coins = dfs(curr.left)
            right_coins = dfs(curr.right)

            result += abs(left_coins) + abs(right_coins)

            return (curr.val - 1) + left_coins + right_coins

        dfs(root)

        return result


tests = [
    [build_tree_from_list([3,0,0]), 2],
    [build_tree_from_list([0,3,0]), 3],
]

run_functional_tests(Solution().distributeCoins, tests)
