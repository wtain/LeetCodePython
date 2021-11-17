"""
https://leetcode.com/problems/delete-nodes-and-return-forest/

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.



Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]


Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
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
from Common.TreeUtils import build_tree_from_list, build_tree_list_from_lists


# Runtime: 68 ms, faster than 70.57% of Python3 online submissions for Delete Nodes And Return Forest.
# Memory Usage: 15 MB, less than 26.75% of Python3 online submissions for Delete Nodes And Return Forest.
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)

        def impl(node: TreeNode, parent: TreeNode, is_left: bool, add: bool):
            nonlocal result, to_delete
            if not node:
                return
            if node.val in to_delete:
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
                impl(node.left, node, True, True)
                impl(node.right, node, False, True)
            else:
                if add:
                    result.append(node)
                impl(node.left, node, True, False)
                impl(node.right, node, False, False)

        impl(root, None, False, True)

        return result


tests = [
    [build_tree_from_list([1,2,3,4,5,6,7]), [3,5], build_tree_list_from_lists([[1,2,null,4],[6],[7]])],
    [build_tree_from_list([1,2,4,null,3]), [3], build_tree_list_from_lists([[1,2,4]])]
]

run_functional_tests(Solution().delNodes, tests)
