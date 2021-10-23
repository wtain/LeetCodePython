"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.



Example 1:


Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:

Input: preorder = [1,3]
Output: [1,null,3]


Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 108
All the values of preorder are unique.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 36 ms, faster than 81.10% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 14.4 MB, less than 44.72% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        n = len(preorder)
        root = TreeNode(preorder[0])
        parents = [root]
        for i in range(1, n):
            if not parents:
                break
            child = TreeNode(preorder[i])
            if parents[-1].val > preorder[i]:
                parents[-1].left = child
                parents.append(child)
            else:
                prevParent = None
                while len(parents) > 1 and parents[-1].val < preorder[i]:
                    prevParent = parents.pop()
                if prevParent and parents[-1].val > preorder[i]:
                    parents.append(prevParent)
                while parents[-1].right and parents[-1].val < preorder[i]:
                    parents.append(parents[-1].right)
                parents[-1].right = child
                parents.append(child)
        return root


tests = [
    [
        [8,5,1,7,10,12],
        build_tree_from_list([8,5,10,1,7,null,12])
    ],
    [
        [1,3],
        build_tree_from_list([1,null,3])
    ]
]

run_functional_tests(Solution().bstFromPreorder, tests)