"""
https://leetcode.com/problems/cousins-in-binary-tree/

nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
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


# Runtime: 36 ms, faster than 52.28% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 14.4 MB, less than 41.10% of Python3 online submissions for Cousins in Binary Tree.
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xr, yr = [None, -1], [None, -1]

        def get_depth(current: TreeNode, parent: TreeNode, current_depth: int):
            nonlocal x, y, xr, yr
            while current:
                if current.val == x:
                    xr = [parent, current_depth]
                if current.val == y:
                    yr = [parent, current_depth]
                get_depth(current.left, current, current_depth+1)
                if xr[0] and yr[0]:
                    return
                parent = current
                current = current.right
                current_depth += 1

        get_depth(root, None, 0)
        return xr[0] != yr[0] and xr[1] == yr[1]


tests = [
    [build_tree_from_list([1,2,3,4]), 4, 3, False],
    [build_tree_from_list([1,2,3,null,4,null,5]), 5, 4, True],
    [build_tree_from_list([1,2,3,null,4]), 2, 3, False]
]

run_functional_tests(Solution().isCousins, tests)