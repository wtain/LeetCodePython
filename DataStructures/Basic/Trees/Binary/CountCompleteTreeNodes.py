"""
https://leetcode.com/problems/count-complete-tree-nodes/

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests, convert_test_params
from Common.TreeUtils import build_tree_from_list


# Runtime: 104 ms, faster than 35.24% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.6 MB, less than 15.78% of Python3 online submissions for Count Complete Tree Nodes.
# https://leetcode.com/submissions/detail/357305248/
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countSize(root: TreeNode, l: bool) -> int:
            r = 0
            while root:
                r += 1
                root = root.left if l else root.right
            return r
        hl, hr = countSize(root, True), countSize(root, False)
        if hl == hr:
            return (1 << hl) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


tests = [
    [[1,2,3,4,5,6], 6],
    [[], 0],
    [[1], 1],
]

run_functional_tests(Solution().countNodes, convert_test_params(tests, build_tree_from_list, indexes=[0]))