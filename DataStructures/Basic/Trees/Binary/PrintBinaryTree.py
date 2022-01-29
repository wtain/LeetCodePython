"""
https://leetcode.com/problems/print-binary-tree/

Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.



Example 1:


Input: root = [1,2]
Output:
[["","1",""],
 ["2","",""]]
Example 2:


Input: root = [1,2,3,null,4]
Output:
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]


Constraints:

The number of nodes in the tree is in the range [1, 210].
-99 <= Node.val <= 99
The depth of the tree will be in the range [1, 10].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 36 ms, faster than 71.46% of Python3 online submissions for Print Binary Tree.
# Memory Usage: 14.3 MB, less than 54.08% of Python3 online submissions for Print Binary Tree.
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return []

        def get_height(node: TreeNode) -> int:
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        height = get_height(root)
        m = height + 1
        n = 1 << m - 1
        m -= 1
        n -= 1

        canvas = [[''] * n for _ in range(m)]

        i0, j0 = 0, n // 2

        def draw(node: TreeNode, i: int, j: int, row: int):
            nonlocal canvas, height
            canvas[i][j] = str(node.val)
            if node.left:
                draw(node.left, i+1, j-(1 << (height - row-2)), row+1)
            if node.right:
                draw(node.right, i+1, j+(1 << (height - row-2)), row+1)

        draw(root, i0, j0, 0)

        return canvas


tests = [
    [
        build_tree_from_list([1,2]),
        [["","1",""],
         ["2","",""]]
    ],
    [
        build_tree_from_list([1,2,3,null,4]),
        [["","","","1","","",""],
         ["","2","","","","3",""],
         ["","","4","","","",""]]
    ]
]

run_functional_tests(Solution().printTree, tests)
