"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3819/
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]




Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Constraints:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""


# Definition for a binary tree node.
from typing import List

from Common.Leetcode import TreeNode

"""
Runtime: 164 ms, faster than 5.25% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 17.7 MB, less than 75.52% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""
# class Solution:
#
#     def getPath(self, root: TreeNode, p: TreeNode) -> List[TreeNode]:
#         def getPathImpl(root: TreeNode, p: TreeNode, path: List[TreeNode]):
#             path.append(root)
#             if root is p:
#                 return True
#             if root.left and getPathImpl(root.left, p, path):
#                 return True
#             if root.right and getPathImpl(root.right, p, path):
#                 return True
#             path.pop()
#             return False
#
#         path: List[TreeNode] = []
#         getPathImpl(root, p, path)
#         return path
#
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         path1: List[TreeNode] = self.getPath(root, p)
#         path2: List[TreeNode] = self.getPath(root, q)
#         n1 = len(path1)
#         n2 = len(path2)
#         i1 = n1-1
#         i2 = n2-1
#         while i2 > i1:
#             i2 -= 1
#         while i1 > i2:
#             i1 -= 1
#         while path1[i1] is not path2[i2]:
#             i1 -= 1
#             i2 -= 1
#         return path2[i1]


# Runtime: 80 ms, faster than 55.25% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.2 MB, less than 79.58% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < q.val and node.val < p.val:
                node = node.right
            else:
                return node


t1 = TreeNode(6)
n1 = t1.left = TreeNode(2)
n2 = t1.right = TreeNode(8)

t1.left.left = TreeNode(0)
n3 = t1.left.right = TreeNode(4)

t1.left.right.left = TreeNode(3)
t1.left.right.right = TreeNode(5)

t1.right.left = TreeNode(7)
t1.right.right = TreeNode(9)

print(Solution().lowestCommonAncestor(t1, n1, n2).val)  # 6

print(Solution().lowestCommonAncestor(t1, n1, n3).val)  # 2
