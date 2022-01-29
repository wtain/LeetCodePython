"""
https://leetcode.com/problems/recover-binary-search-tree/

You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?



Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from Common.Constants import null
from Common.Helpers.FunctionalHelpers import make_inplace
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def find_wrong(root: TreeNode, found: List[TreeNode], l, r):
#             if not root:
#                 return
#             if root.left and root.val < root.left.val or root.right and root.val > root.right.val or \
#                     l and root.val <= l or \
#                     r and root.val >= r:
#                 found.append(root)
#             find_wrong(root.left, found, l, root.val)
#             find_wrong(root.right, found, root.val, r)
#
#         found = []
#         find_wrong(root, found, None, None)
#         print([v.val for v in found])


# Runtime: 72 ms, faster than 75.04% of Python3 online submissions for Recover Binary Search Tree.
# Memory Usage: 14.8 MB, less than 19.84% of Python3 online submissions for Recover Binary Search Tree.
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, first, second = None, None, None

        def inorder(node: TreeNode):
            nonlocal prev, first, second
            if node.left:
                inorder(node.left)

            if not first and (not prev or node.val < prev.val):
                first = prev
            if first and (not prev or node.val < prev.val):
                second = node

            prev = node
            if node.right:
                inorder(node.right)

        inorder(root)
        first.val, second.val = second.val, first.val


tests = [
    [
        TreeNode(1,
                 TreeNode(3,
                          null,
                          TreeNode(2))),
        TreeNode(3,
                 TreeNode(1,
                          null,
                          TreeNode(2)))
    ],
    [
        TreeNode(3,
                 TreeNode(1),
                 TreeNode(4,
                          TreeNode(2))),
        TreeNode(2,
                 TreeNode(1),
                 TreeNode(4,
                          TreeNode(3)))
    ]
]

run_functional_tests(make_inplace(Solution().recoverTree), tests)