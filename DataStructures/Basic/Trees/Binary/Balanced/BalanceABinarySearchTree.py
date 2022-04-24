"""
https://leetcode.com/problems/balance-a-binary-search-tree/

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
from typing import List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.Helpers.FunctionalHelpers import make_inplace
from Common.Helpers.TestParamsHelpers import convert_test_params
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list, is_balanced


# class Solution:
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#
#         def first_node(node: TreeNode) -> (TreeNode, List[TreeNode]):
#             if not node:
#                 return None, []
#             parents = []
#             while node.left:
#                 parents.append(node)
#                 node = node.left
#             return node, parents
#
#         def next_node(node: TreeNode, parents: List[TreeNode]) -> (TreeNode, List[TreeNode]):
#             if not node:
#                 return None, []
#             if node.right:
#                 node1, parents1 = first_node(node.right)
#                 return node1, parents + parents1
#             while parents:
#                 parent = parents.pop()
#                 if parent.left == node:
#                     return parent, parents
#                 node = parent
#             return None
#
#         slow, slow_parents = first_node(root)
#         fast, fast_parents = slow, copy.copy(slow_parents)
#         while fast:
#             slow, slow_parents = next_node(slow, slow_parents)
#             fast, fast_parents = next_node(fast, fast_parents)
#             if not fast:
#                 break
#             fast, fast_parents = next_node(fast, fast_parents)
#
#         return root


# WRONG
# class Solution:
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#         def depth(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             return 1 + max(depth(root.left), depth(root.right))
#
#         if not root:
#             return root
#
#         dl, dr = depth(root.left), depth(root.right)
#
#         if abs(dl-dr) <= 1:
#             return root
#         if dl > dr:
#             l = root.left
#             ll, lr = self.balanceBST(l.left), self.balanceBST(l.right)
#             l.right = root
#             root.left = lr
#             root.right = self.balanceBST(root.right)
#             return l
#         else:
#             r = root.right
#             rl, rr = self.balanceBST(r.left), self.balanceBST(r.right)
#             r.left = root
#             root.right = rl
#             root.left = self.balanceBST(root.left)
#             return r

# Runtime: 329 ms, faster than 94.22% of Python3 online submissions for Balance a Binary Search Tree.
# Memory Usage: 19.5 MB, less than 80.53% of Python3 online submissions for Balance a Binary Search Tree.
# https://leetcode.com/problems/balance-a-binary-search-tree/discuss/1973245/Easy-Clean-Code-or-O(n)-Time-or-Proper-In-place-O(1)-Space-or-Only-recursion-space
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        head, prev = None, None

        def sorted_doubly_linked_list_from_bst(root: TreeNode):
            nonlocal head, prev
            if not root:
                return root
            sorted_doubly_linked_list_from_bst(root.left)
            if not head:
                head = root
            else:
                prev.right = root
            root.left = prev
            prev = root
            sorted_doubly_linked_list_from_bst(root.right)

        def balance_bst_from_double_linked_list(head: TreeNode) -> TreeNode:
            if not head:
                return head
            if not head.left and not head.right:
                return head
            slow, fast = head, head
            while fast and fast.right:
                slow = slow.right
                fast = fast.right.right
            root = slow
            if root.left:
                root.left.right = None
            root.left = balance_bst_from_double_linked_list(head)
            if slow.right:
                slow.right.left = None
            root.right = balance_bst_from_double_linked_list(slow.right)
            return root

        sorted_doubly_linked_list_from_bst(root)
        return balance_bst_from_double_linked_list(head)


tests = [
    [[1,null,2,null,3,null,4,null,null], [2,1,3,null,null,null,4]],
    [[2,1,3], [2,1,3]],
    [[1,null,2,null,3,null,5,4], [3,1,4,null,2,null,5]]
]

run_functional_tests(Solution().balanceBST, convert_test_params(tests, build_tree_from_list), custom_check=lambda test, result: is_balanced(result))
