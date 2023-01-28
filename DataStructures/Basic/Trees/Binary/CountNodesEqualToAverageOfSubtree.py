"""
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.


Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation:
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:


Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
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
# 98 ms
# Beats
# 30.5%
# Memory
# 15.2 MB
# Beats
# 69.28%
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count_equal_to_subtree_average = 0

        def dfs(node: TreeNode) -> (int, int):
            nonlocal count_equal_to_subtree_average
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            sum = left_sum + right_sum + node.val
            count = left_count + right_count + 1
            if node.val == sum // count:
                count_equal_to_subtree_average += 1
            return sum, count

        dfs(root)

        return count_equal_to_subtree_average


tests = [
    [build_tree_from_list([4,8,5,0,1,null,6]), 5],
    [build_tree_from_list([1]), 1],
]

run_functional_tests(Solution().averageOfSubtree, tests)
