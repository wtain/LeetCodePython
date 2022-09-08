"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
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


# Runtime: 60 ms, faster than 17.62% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14 MB, less than 13.48% of Python3 online submissions for Binary Tree Inorder Traversal.
# https://leetcode.com/submissions/detail/182712378/
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def first(root: TreeNode, parents: List[TreeNode]) -> TreeNode:
            while root.left:
                parents.append(root)
                root = root.left
            return root

        def right_parent(root: TreeNode, parents: List[TreeNode]) -> TreeNode:
            current = root
            while parents:
                parent = parents.pop()
                if id(parent.left) == id(current):
                    return parent
                current = parent
            return None

        result = []
        parents = []
        current = first(root, parents)
        while current:
            result.append(current.val)
            if current.right:
                parents.append(current)
                current = first(current.right, parents)
            else:
                if parents:
                    current = right_parent(current, parents)
                else:
                    current = None

        return result


tests = [
    [build_tree_from_list([3,1,null,null,2]), [1,2,3]],

    [build_tree_from_list([1,null,2,3]), [1,3,2]],
    [build_tree_from_list([]), []],
    [build_tree_from_list([1]), [1]],
]

run_functional_tests(Solution().inorderTraversal, tests)
