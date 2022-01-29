"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/607/week-5-june-29th-june-30th/3797/
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 76 ms, faster than 48.91% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 27.3 MB, less than 38.05% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#
#         def get_path(root: TreeNode, node: TreeNode) -> List[TreeNode]:
#             def impl(root: TreeNode, node: TreeNode, path: List[TreeNode]) -> bool:
#                 if not root:
#                     return False
#                 if root == node:
#                     path.append(root)
#                     return True
#                 if impl(root.left, node, path) or impl(root.right, node, path):
#                     path.append(root)
#                     return True
#                 return False
#             path = []
#             impl(root, node, path)
#             return path
#
#         p1, p2 = get_path(root, p), get_path(root, q)
#         n1, n2 = len(p1), len(p2)
#         i, j = n1-1, n2-1
#
#         result = root
#         while i >= 0 and j >= 0:
#             if p1[i] == p2[j]:
#                 result = p1[i]
#             else:
#                 return result
#             i -= 1
#             j -= 1
#         return result


# Runtime: 84 ms, faster than 26.25% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 27.2 MB, less than 38.05% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#
#         def get_path(root: TreeNode, node: TreeNode) -> List[TreeNode]:
#             def impl(root: TreeNode, node: TreeNode, path: List[TreeNode]) -> bool:
#                 if not root:
#                     return False
#                 if root == node:
#                     path.append(root)
#                     return True
#                 if impl(root.left, node, path) or impl(root.right, node, path):
#                     path.append(root)
#                     return True
#                 return False
#             path = []
#             impl(root, node, path)
#             return path
#
#         p1, p2 = get_path(root, p), get_path(root, q)
#         n1, n2 = len(p1), len(p2)
#         i, j = n1-1, n2-1
#
#         result = root
#         while i >= 0 and j >= 0 and p1[i] == p2[j]:
#             result = p1[i]
#             i -= 1
#             j -= 1
#         return result


# Runtime: 72 ms, faster than 68.29% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 18.3 MB, less than 89.71% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        st = [(root, 0)]
        one_found = False
        index = -1
        while st:
            node, n_found = st[-1]
            if n_found != 2:
                if n_found == 0:
                    if node == p or node == q:
                        if one_found:
                            return st[index][0]
                        else:
                            one_found = True
                            index = len(st)-1
                    child = node.left
                else:
                    child = node.right
                st.pop()
                st.append((node, n_found+1))
                if child:
                    st.append((child, 0))
            else:
                if one_found and index == len(st)-1:
                    index -= 1
                st.pop()
        return None


p4 = TreeNode(4)

p2 = TreeNode(2,
                     TreeNode(7),
                     p4)

p5 = TreeNode(5,
                TreeNode(6),
                p2)

p1 = TreeNode(1,
                TreeNode(0),
                TreeNode(8))

tree = TreeNode(3, p5, p1)

t2 = TreeNode(2)
t1 = TreeNode(1,
              t2)

tests = [
    [
        tree,
        p5, p1,
        tree
    ],
    [
        tree,
        p5, p4,
        p5
    ],
    [
        t1,
        t1, t2,
        t1
    ]
]

run_functional_tests(Solution().lowestCommonAncestor, tests)