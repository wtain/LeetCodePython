"""
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.



Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
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


# Runtime: 351 ms, faster than 70.29% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 18 MB, less than 81.53% of Python3 online submissions for All Elements in Two Binary Search Trees.
# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#
#         result = []
#
#         def find_first(root: TreeNode) -> List[TreeNode]:
#             node_and_parents = []
#             if not root:
#                 return node_and_parents
#             node = root
#             node_and_parents.append(root)
#             while node.left:
#                 node = node.left
#                 node_and_parents.append(node)
#             return node_and_parents
#
#         def get_next(node_and_parents: List[TreeNode]) -> List[TreeNode]:
#             current = node_and_parents.pop()
#             if current.right:
#                 node_and_parents += find_first(current.right)
#             return node_and_parents
#
#         def impl(root1: TreeNode, root2: TreeNode):
#             nonlocal result
#             c1, c2 = find_first(root1), find_first(root2)
#             while c1 or c2:
#                 if c1 and c2:
#                     if c1[-1].val < c2[-1].val:
#                         result.append(c1[-1].val)
#                         c1 = get_next(c1)
#                     else:
#                         result.append(c2[-1].val)
#                         c2 = get_next(c2)
#                 elif c1:
#                     result.append(c1[-1].val)
#                     c1 = get_next(c1)
#                 else:
#                     result.append(c2[-1].val)
#                     c2 = get_next(c2)
#
#         impl(root1, root2)
#         return result

# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         result = []
#
#         def impl(node1: TreeNode, node2: TreeNode):
#             nonlocal result
#             if node1 and node2:
#                 if node1.val < node2.val:
#                     impl(node1.left, node2)
#                 else:
#                     impl(node1, node2.left)
#             elif node1:
#                 impl(node1.left, node2)
#                 result.append(node1.val)
#                 impl(node1.right, node2)
#             elif node2:
#                 impl(node1, node2.left)
#                 result.append(node2.val)
#                 impl(node1, node2.right)
#
#         impl(root1, root2)
#
#         return result


# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         result = []
#
#         def impl(node1: TreeNode, node2: TreeNode):
#             nonlocal result
#             if not node1 and not node2:
#                 return
#             if not node2:
#                 impl(node1.left, None)
#                 result.append(node1.val)
#                 impl(node1.right, None)
#                 return
#             if not node1:
#                 impl(node2.left, None)
#                 result.append(node2.val)
#                 impl(node2.right, None)
#                 return
#             if node1.val < node2.val:
#                 impl(node1, node2.left)
#                 impl(node2, node1.right)
#             else:
#                 impl(node2, node1.left)
#                 impl(node1, node2.right)
#
#         impl(root1, root2)
#         return result


# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         result = []
#
#         def is_leaf(node: TreeNode) -> bool:
#             return not node.left and not node.right;
#
#         def impl(node1: TreeNode, node2: TreeNode) -> int:
#             nonlocal result
#             if not node1 and not node2:
#                 return 0
#             if not node1:
#                 result.append(node2.val)
#                 return 2
#             if not node2:
#                 result.append(node1.val)
#                 return 1
#             if is_leaf(node1) and is_leaf(node2):
#                 if node1.val < node2.val:
#                     result.append(node1.val)
#                     return 1
#                 else:
#                     result.append(node2.val)
#                     return 2
#
#
#         impl(root1, root2)
#
#         return result

# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#
#         result = []
#
#         def go_left(node1: TreeNode, node2: TreeNode):
#             nonlocal result
#
#         def impl(node1: TreeNode, node2: TreeNode):
#             nonlocal result
#             if node1 and node2:
#                 go_left(node1.left, node2.left)
#
#
#
#         impl(root1, root2)
#         return result


# Runtime: 706 ms, faster than 12.15% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 18 MB, less than 90.87% of Python3 online submissions for All Elements in Two Binary Search Trees.
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/1722528/C%2B%2B-O(n1-%2B-n2)-time-O(1)-space-with-general-Morris-inorder-simulation
class Solution:

    class MorrisTreeTransformation:

        def __init__(self, root: TreeNode):
            self.root = root
            self.nxt = root
            self.next()

        def poll(self):
            if not self.root:
                return None
            res = self.root
            self.next()
            return res

        def peek(self):
            return self.root

        def has_next(self):
            return self.root

        def next(self):
            self.root = self.nxt
            while self.has_next():
                if self.root.left:
                    pre = self.root.left
                    while pre.right and pre.right != self.root:
                        pre = pre.right
                    if pre.right:
                        pre.right = None
                        self.nxt = self.root.right
                        break
                    else:
                        pre.right = self.root
                        self.root = self.root.left
                else:
                    self.nxt = self.root.right
                    break

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        t1, t2 = self.MorrisTreeTransformation(root1), self.MorrisTreeTransformation(root2)
        while t1.has_next() and t2.has_next():
            if t1.peek().val < t2.peek().val:
                result.append(t1.poll().val)
            else:
                result.append(t2.poll().val)
        while t1.has_next():
            result.append(t1.poll().val)
        while t2.has_next():
            result.append(t2.poll().val)
        return result


tests = [
    [build_tree_from_list([2,1,4]), build_tree_from_list([1,0,3]), [0,1,1,2,3,4]],
    [build_tree_from_list([1,null,8]), build_tree_from_list([8,1]), [1,1,8,8]],
]

run_functional_tests(Solution().getAllElements, tests)
