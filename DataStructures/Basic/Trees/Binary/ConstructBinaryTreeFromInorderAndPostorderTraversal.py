"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 60 ms, faster than 73.90% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
# Memory Usage: 20.1 MB, less than 47.28% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        idx_in = {v: i for i, v in enumerate(inorder)}

        def impl(in1: int, in2: int, post1: int, post2: int) -> TreeNode:
            if in1 == in2 or post1 == post2:
                return None
            v = postorder[post2-1]
            node = TreeNode(v)
            inN = idx_in[v]
            Ain1, Ain2, Bin1, Bin2 = in1, inN, inN+1, in2
            nA = Ain2 - Ain1
            Apost1, Apost2, Bpost2 = post1, post1+nA, post2-1
            Bpost1 = Apost2
            node.left = impl(Ain1, Ain2, Apost1, Apost2)
            node.right = impl(Bin1, Bin2, Bpost1, Bpost2)
            return node

        return impl(0, len(inorder), 0, len(postorder))


tests = [
    [[9,3,15,20,7], [9,15,7,20,3], build_tree_from_list([3,9,20,null,null,15,7])],
    [[-1], [-1], build_tree_from_list([-1])],
]

run_functional_tests(Solution().buildTree, tests)
