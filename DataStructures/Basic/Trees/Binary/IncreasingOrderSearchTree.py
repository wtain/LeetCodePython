"""
https://leetcode.com/problems/increasing-order-search-tree/

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Runtime: 29 ms, faster than 91.75% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 13.9 MB, less than 90.59% of Python3 online submissions for Increasing Order Search Tree.
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def impl(root: TreeNode) -> (TreeNode, TreeNode):
            if not root:
                return None, None
            pleft, pright = impl(root.left), impl(root.right)
            pmin = pleft[0] or root
            pmax = pright[1] or root

            if pleft[1]:
                pleft[1].right = root
            root.right = pright[0]
            root.left = None
            return pmin, pmax

        return impl(root)[0]


tests = [
    [
        build_tree_from_list([5,3,6,2,4,null,8,1,null,null,null,7,9]),
        build_tree_from_list([1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9])
    ],
    [
        build_tree_from_list([5,1,7]),
        build_tree_from_list([1,null,5,null,7])
    ]
]

run_functional_tests(Solution().increasingBST, tests)

