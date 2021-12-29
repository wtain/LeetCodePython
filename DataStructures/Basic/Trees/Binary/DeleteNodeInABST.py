"""
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.


Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105


Follow up: Could you solve it with time complexity O(height of tree)?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list, is_bst, in_bst, bst_values


# Runtime: 100 ms, faster than 17.95% of Python3 online submissions for Delete Node in a BST.
# Memory Usage: 18.5 MB, less than 22.29% of Python3 online submissions for Delete Node in a BST.
# https://leetcode.com/submissions/detail/388896739/
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#
#         def find_min(node: TreeNode, parent: TreeNode, is_right: bool) -> (TreeNode, TreeNode, bool):
#             while node.left:
#                 parent, node, is_right = node, node.left, False
#             return node, parent, is_right
#
#         def find_max(node: TreeNode, parent: TreeNode, is_right: bool) -> (TreeNode, TreeNode, bool):
#             while node.right:
#                 parent, node, is_right = node, node.right, True
#             return node, parent, is_right
#
#         if not root:
#             return None
#
#         parent, is_right = None, False
#
#         node = root
#         while node:
#             if node.val == key:
#                 if node.right:
#                     min_node, min_parent, min_is_right = find_min(node.right, node, True)
#                     min_right = min_node.right
#                     if min_is_right:
#                         min_parent.right = min_right
#                     else:
#                         min_parent.left = min_right
#                     if min_node.right != node.right:
#                         min_node.right = node.right
#                     min_node.left = node.left
#                     if parent:
#                         if is_right:
#                             parent.right = min_node
#                         else:
#                             parent.left = min_node
#                     return root if parent else min_node
#                 elif node.left:
#                     max_node, max_parent, max_is_right = find_max(node.left, node, False)
#                     min_left = max_node.left
#                     if max_is_right:
#                         max_parent.right = min_left
#                     else:
#                         max_parent.left = min_left
#                     if max_node.left != node.left:
#                         max_node.left = node.left
#                     max_node.right = node.right
#                     if parent:
#                         if is_right:
#                             parent.right = max_node
#                         else:
#                             parent.left = max_node
#                     return root if parent else max_node
#                 else:
#                     if parent:
#                         if is_right:
#                             parent.right = None
#                         else:
#                             parent.left = None
#                     return root if parent else None
#             parent = node
#             if node.val < key:
#                 is_right = True
#                 node = node.right
#             else:
#                 is_right = False
#                 node = node.left
#
#         return root

# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         FIND_NONE, FIND_MIN, FIND_MAX = 0, 1, 2
#         # remove?, min/max, parent, left, right
#         def impl(node: TreeNode, parent: TreeNode, find_min_max: int) -> (bool, TreeNode, TreeNode, TreeNode, TreeNode):
#             if node.val == key:
#                 if node.left:
#                     impl(node.left, node, FIND_MAX)
#                 elif node.right:
#                 else:
#                     return True, None, parent, None


# WRONG
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         def find_node(node: TreeNode, parent: TreeNode, key: int) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if key == node.val:
#                 return node, parent
#             if key < node.val:
#                 return find_node(node.left, node, key)
#             return find_node(node.right, node, key)
#
#         def find_min(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.left:
#                 return node, parent
#             return find_min(node.left, node)
#
#         def find_max(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.right:
#                 return node, parent
#             return find_max(node.right, node)
#
#         node, parent = find_node(root, None, key)
#         if not node:
#             return root
#
#         if not parent:
#             if node.left:
#                 max_node, max_parent = find_max(node.left, node)
#                 max_parent.right = None
#                 max_node.left = node.left
#                 max_node.right = node.right
#                 return max_node
#             if node.right:
#                 min_node, min_parent = find_min(node.right, node)
#                 min_parent.left = None
#                 min_node.left = node.left
#                 min_node.right = node.right
#                 return min_node
#             return None
#
#         if parent.val > node.val:
#             parent.left = None
#         else:
#             parent.right = None
#
#         new_root = None
#
#         if node.left:
#             max_node, max_parent = find_max(node.left, node)
#             max_parent.right = None
#             max_node.left = node.left
#             max_node.right = node.right
#             new_root = max_node
#         elif node.right:
#             min_node, min_parent = find_min(node.right, node)
#             min_parent.left = None
#             min_node.left = node.left
#             min_node.right = node.right
#             new_root = min_node
#         if parent.val > node.val:
#             if parent != new_root and new_root:
#                 parent.left = new_root
#         else:
#             if parent != new_root and new_root:
#                 parent.right = new_root
#         return root



# WRONG
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         def find_node(node: TreeNode, parent: TreeNode, key: int) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if key == node.val:
#                 return node, parent
#             if key < node.val:
#                 return find_node(node.left, node, key)
#             return find_node(node.right, node, key)
#
#         def find_min(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.left:
#                 return node, parent
#             return find_min(node.left, node)
#
#         def find_max(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.right:
#                 return node, parent
#             return find_max(node.right, node)
#
#         node, parent = find_node(root, None, key)
#         if not node:
#             return root
#
#         if not parent:
#             if node.left:
#                 max_node, max_parent = find_max(node.left, node)
#                 max_parent.right = None
#                 max_node.left = node.left
#                 max_node.right = node.right
#                 return max_node
#             if node.right:
#                 min_node, min_parent = find_min(node.right, node)
#                 min_parent.left = None
#                 min_node.left = node.left
#                 min_node.right = node.right
#                 return min_node
#             return None
#
#         if parent.val > node.val:
#             parent.left = None
#
#             max_node = None
#             if node.right:
#                 max_node, max_parent = find_max(node.right, node)
#             elif node.left:
#                 max_node, max_parent = find_max(node.left, node)
#
#             if max_node:
#                 max_parent.right = None
#                 max_node.left = node.left
#                 max_node.right = node.right
#                 parent.left = max_node
#         else:
#             parent.right = None
#
#             min_node = None
#             if node.left:
#                 min_node, min_parent = find_max(node.left, node)
#                 min_parent.right = None
#             elif node.right:
#                 min_node, min_parent = find_min(node.right, node)
#                 min_parent.left = None
#
#             if min_node:
#                 min_node.left = node.left
#                 min_node.right = node.right
#                 parent.right = min_node
#
#         return root


# WRONG
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         def find_node(node: TreeNode, parent: TreeNode, key: int) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if key == node.val:
#                 return node, parent
#             if key < node.val:
#                 return find_node(node.left, node, key)
#             return find_node(node.right, node, key)
#
#         def find_min(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.left:
#                 return node, parent
#             return find_min(node.left, node)
#
#         def find_max(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.right:
#                 return node, parent
#             return find_max(node.right, node)
#
#         node, parent = find_node(root, None, key)
#         if not node:
#             return root
#
#         if not parent:
#             if node.left:
#                 max_node, max_parent = find_max(node.left, node)
#                 max_parent.right = None
#                 max_node.left = node.left
#                 max_node.right = node.right
#                 return max_node
#             if node.right:
#                 min_node, min_parent = find_min(node.right, node)
#                 min_parent.left = None
#                 min_node.left = node.left
#                 min_node.right = node.right
#                 return min_node
#             return None
#
#         if parent.val > node.val:
#             parent.left = None
#
#             max_node = None
#             if node.right:
#                 max_node, max_parent = find_max(node.right, node)
#             elif node.left:
#                 max_node, max_parent = find_max(node.left, node)
#
#             if max_node:
#                 max_parent.right = None
#                 max_node.left = node.left
#                 max_node.right = node.right
#                 parent.left = max_node
#         else:
#             parent.right = None
#
#             min_node = None
#             if node.left:
#                 min_node, min_parent = find_max(node.left, node)
#                 min_parent.right = None
#             elif node.right:
#                 min_node, min_parent = find_min(node.right, node)
#                 min_parent.left = None
#
#             if min_node:
#                 min_node.left = node.left
#                 min_node.right = node.right
#                 parent.right = min_node
#
#         return root



# WRONG
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         def find_node(node: TreeNode, parent: TreeNode, key: int) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if key == node.val:
#                 return node, parent
#             if key < node.val:
#                 return find_node(node.left, node, key)
#             return find_node(node.right, node, key)
#
#         def find_min(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.left:
#                 return node, parent
#             return find_min(node.left, node)
#
#         def find_max(node: TreeNode, parent: TreeNode) -> (TreeNode, TreeNode):
#             if not node:
#                 return None, None
#             if not node.right:
#                 return node, parent
#             return find_max(node.right, node)
#
#         node, parent = find_node(root, None, key)
#         if not node:
#             return root
#
#         if not parent:
#             if not node.left:
#                 return node.right
#             if not node.right:
#                 return node.left
#             if node.left:
#                 max_node, max_parent = find_max(node.left, node)
#                 if max_parent != node:
#                     max_parent.right = None
#                 if max_node != node.left:
#                     max_node.left = node.left
#                 if max_node != node.right:
#                     max_node.right = node.right
#                 return max_node
#             if node.right:
#                 min_node, min_parent = find_min(node.right, node)
#                 if min_parent != node:
#                     min_parent.left = None
#                 if min_node != node.left:
#                     min_node.left = node.left
#                 if min_node != node.right:
#                     min_node.right = node.right
#                 return min_node
#             return None
#
#         if parent.val < node.val:
#
#             if not node.left:
#                 parent.right = node.right
#                 return root
#             if not node.right:
#                 parent.right = node.left
#                 return root
#
#             parent.right = None
#
#             min_node = None
#             if node.left:
#                 min_node, min_parent = find_max(node.left, node)
#                 if min_parent != node:
#                     min_parent.right = None
#             elif node.right:
#                 min_node, min_parent = find_min(node.right, node)
#                 if min_parent != node:
#                     min_parent.left = None
#
#             if min_node:
#                 if node.left != min_node:
#                     min_node.left = node.left
#                 if node.right != min_node:
#                     min_node.right = node.right
#                 parent.right = min_node
#         else:
#             if not node.left:
#                 parent.left = node.right
#                 return root
#             if not node.right:
#                 parent.left = node.left
#                 return root
#
#             parent.left = None
#
#             max_node = None
#             if node.right:
#                 max_node, max_parent = find_min(node.right, node)
#                 if max_parent != node:
#                     max_parent.left = None
#             elif node.left:
#                 max_node, max_parent = find_max(node.left, node)
#                 if max_parent != node:
#                     max_parent.right = None
#
#             if max_node:
#                 if max_node != node.left:
#                     max_node.left = node.left
#                 if max_node != node.right:
#                     max_node.right = node.right
#                 parent.left = max_node
#
#         return root


# Runtime: 79 ms, faster than 60.26% of Python3 online submissions for Delete Node in a BST.
# Memory Usage: 18.4 MB, less than 64.86% of Python3 online submissions for Delete Node in a BST.
# https://leetcode.com/problems/delete-node-in-a-bst/discuss/1583492/C%2B%2B-or-91-Faster-or-Recursive-Solution
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = root.left
            while node and node.right:
                node = node.right
            node.right = root.right
            return root.left
        return root


tests = [
    [build_tree_from_list([5,3,6,2,4,null,7]), 3, build_tree_from_list([5,4,6,2,null,null,7])],
    [build_tree_from_list([5,3,6,2,4,null,7]), 0, build_tree_from_list([5,3,6,2,4,null,7])],
    [None, 0, None],
    [build_tree_from_list([5,3,6,2,4,null,7]), 5, build_tree_from_list([6,3,7,2,4])],
    [build_tree_from_list([5,3,6,2,4,null,7]), 7, build_tree_from_list([5,3,6,2,4])],
    [build_tree_from_list([0]), 0, None],
    [build_tree_from_list([4,null,7,6,8,5,null,null,9]), 7, build_tree_from_list([4,null,8,6,9,5])],
    [build_tree_from_list([1,null,2]), 1, build_tree_from_list([2])],
    [build_tree_from_list([5,3,6,2,4,null,7]), 5, build_tree_from_list([6,3,7,2,4])],
    [
        build_tree_from_list([8,0,31,null,6,28,45,1,7,25,30,32,49,null,4,null,null,9,26,29,null,null,42,47,null,2,5,null,12,null,27,null,null,41,43,46,48,null,3,null,null,10,19,null,null,33,null,null,44,null,null,null,null,null,null,null,11,18,20,null,37,null,null,null,null,14,null,null,22,36,38,13,15,21,24,34,null,null,39,null,null,null,16,null,null,23,null,null,35,null,40,null,17]), 1,
        build_tree_from_list([8,0,31,null,6,28,45,2,7,25,30,32,49,null,4,null,null,9,26,29,null,null,42,47,null,3,5,null,12,null,27,null,null,41,43,46,48,null,null,null,null,10,19,null,null,33,null,null,44,null,null,null,null,null,11,18,20,null,37,null,null,null,null,14,null,null,22,36,38,13,15,21,24,34,null,null,39,null,null,null,16,null,null,23,null,null,35,null,40,null,17])
    ],
    [
        build_tree_from_list([8, 0, null, null, 6, 1, 7, null, 4, null, null, 2, null, null, 3]), 1,
        build_tree_from_list([8,0,null,null,6,2,7,null,4,null,null,3])
    ],
    [
        build_tree_from_list([6, 1, 7, null, 4, null, null, 2, null, null, 3]), 1,
        build_tree_from_list([6,2,7,null,4,null,null,3])
    ],
    [
        build_tree_from_list([1, null, 4, 2, null, null, 3]), 1,
        build_tree_from_list([2, null,4,3])
    ]
]


def check(test, result) -> bool:
    val = test[1]
    if not is_bst(result):
        return False
    if in_bst(result, val):
        return False
    vals_result = bst_values(result)
    vals_input = bst_values(test[0])
    if val in vals_input:
        vals_input.remove(val)
    return vals_input == vals_result


run_functional_tests(Solution().deleteNode, tests, custom_check=check)
