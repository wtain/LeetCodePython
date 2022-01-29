"""
https://leetcode.com/problems/invert-binary-tree/
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

from typing import List

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params
from Common.TreeUtils import build_tree_from_list

"""
Runtime: 20 ms, faster than 98.67% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.8 MB, less than 51.05% of Python3 online submissions for Invert Binary Tree.
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        toVisit: List[TreeNode] = [root]
        while len(toVisit) > 0:
            nextLevel: List[TreeNode] = []
            for n in toVisit:
                tmp = n.right
                n.right = n.left
                n.left = tmp
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            toVisit = nextLevel
        return root


tests = [
    [[4,2,7,1,3,6,9], [4,7,2,9,6,3,1]],
    [[2,1,3], [2,3,1]],
    [[],[]]
]

run_functional_tests(Solution().invertTree, convert_test_params(tests, build_tree_from_list))