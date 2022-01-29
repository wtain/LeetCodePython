"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.


Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# WRONG
# class Solution:
#     def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
#         counts = []
#
#         def impl(node: TreeNode, level: int) -> (bool, int):
#             nonlocal counts
#             if not node:
#                 return True, 0
#             if level >= len(counts):
#                 counts.append(1)
#             else:
#                 counts[level] += 1
#             if node.right and not node.left:
#                 return False, 0
#             lf, lc = impl(node.left, level + 1)
#             if not lf:
#                 return False, 0
#             rf, rc = impl(node.right, level + 1)
#             if not rf:
#                 return False, 0
#             if rc > lc:
#                 return False, 0
#             return True, 1 + lc + rc
#
#         if not impl(root, 0)[0]:
#             return False
#
#         for i in range(len(counts)-1):
#             if counts[i] != (1 << i):
#                 return False
#
#         return True


# WRONG
# class Solution:
#     def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
#         q = deque()
#         if root:
#             q.append(root)
#
#         while q:
#             next_level = deque()
#             while q:
#                 node = q.popleft()
#                 if not node.left:
#                     if node.right:
#                         return False
#                     break
#                 next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
#                 else:
#                     break
#             if q:
#                 for node in q:
#                     if node.left or node.right:
#                         return False
#             q = next_level
#
#         return True


# Runtime: 32 ms, faster than 89.89% of Python3 online submissions for Check Completeness of a Binary Tree.
# Memory Usage: 14.1 MB, less than 80.39% of Python3 online submissions for Check Completeness of a Binary Tree.
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/1515609/simple-C%2B%2B-solution
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        finished = False

        while q:
            n = q[0]
            if not n:
                finished = True
            elif finished:
                return False
            if n:
                q.append(n.left)
                q.append(n.right)
            q.popleft()

        return True


tests = [
    [build_tree_from_list([1,2,3,4,5,6]), True],
    [build_tree_from_list([1,2,3,4,5,null,7]), False],

    [build_tree_from_list([1,2,3,5,null,7,8]), False],

    [build_tree_from_list([1,2,3,5,null,7]), False],

    [build_tree_from_list([1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]), False]
]


run_functional_tests(Solution().isCompleteTree, tests)
