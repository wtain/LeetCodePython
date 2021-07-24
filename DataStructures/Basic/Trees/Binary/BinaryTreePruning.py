"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3824/
https://leetcode.com/problems/binary-tree-pruning/

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.



Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]


Constraints:

The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 28 ms, faster than 86.42% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 14.4 MB, less than 22.41% of Python3 online submissions for Binary Tree Pruning.
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def impl(node: TreeNode) -> (TreeNode, bool):
            if not node:
                return None, False
            node.left, lf = impl(node.left)
            node.right, rf = impl(node.right)
            if node.val == 1 or lf or rf:
                return node, node.val == 1 or lf or rf
            return None, False

        return impl(root)[0]


tests = [
    [
        TreeNode(1,
                 null,
                 TreeNode(0,
                          TreeNode(0),
                          TreeNode(1))),
        TreeNode(1,
                 null,
                 TreeNode(0,
                          null,
                          TreeNode(1))),
    ],
    [
        TreeNode(1,
                 TreeNode(0,
                          TreeNode(0),
                          TreeNode(0)),
                 TreeNode(1,
                          TreeNode(0),
                          TreeNode(1))),
        TreeNode(1,
                 null,
                 TreeNode(1,
                          null,
                          TreeNode(1)))
    ],
    [
        TreeNode(1,
                 TreeNode(1,
                          TreeNode(1,
                                   TreeNode(0)),
                          TreeNode(1)),
                 TreeNode(0,
                          TreeNode(0),
                          TreeNode(1))),
        TreeNode(1,
                 TreeNode(1,
                          TreeNode(1),
                          TreeNode(1)),
                 TreeNode(0,
                          null,
                          TreeNode(1)))
    ]
]


run_functional_tests(Solution().pruneTree, tests)