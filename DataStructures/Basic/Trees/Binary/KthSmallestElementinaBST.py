"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
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


# Runtime: 59 ms, faster than 74.62% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18.1 MB, less than 48.12% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def min_node(root: TreeNode, parents: List[TreeNode]) -> (TreeNode, List[TreeNode]):
            while root:
                parents.append(root)
                root = root.left
            return parents[-1], parents

        def next_node(node: TreeNode, parents: List[TreeNode]) -> (TreeNode, List[TreeNode]):
            if node.right:
                return min_node(node.right, parents + [node])

            while parents:
                parent = parents.pop()
                if parent.left == node:
                    return parent, parents
                node = parent

            return None, []

        parents = []
        node, parents = min_node(root, parents)
        for i in range(k-1):
            node, parents = next_node(node, parents)

        return node.val


tests = [
    [build_tree_from_list([1,null,2], ), 2, 2],
    [build_tree_from_list([3,1,4,null,2]), 1, 1],
    [build_tree_from_list([5,3,6,2,4,null,null,1]), 3, 3]
]

run_functional_tests(Solution().kthSmallest, tests)
