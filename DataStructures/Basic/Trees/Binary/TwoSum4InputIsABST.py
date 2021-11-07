"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3908/
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.



Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true


Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
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
from Common.ObjectTestingUtils import run_functional_tests, convert_test_params_to_trees


# Runtime: 76 ms, faster than 82.55% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 18.3 MB, less than 42.99% of Python3 online submissions for Two Sum IV - Input is a BST.
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         vals = set()
#
#         def impl(node: TreeNode) -> bool:
#             if not node:
#                 return False
#             m = k - node.val
#             if m in vals:
#                 return True
#             vals.add(node.val)
#             return impl(node.left) or impl(node.right)
#
#         return impl(root)


# Runtime: 80 ms, faster than 68.75% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 16.5 MB, less than 78.45% of Python3 online submissions for Two Sum IV - Input is a BST.
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         p1, p2 = [], []
#         l, r = root, root
#         while l.left:
#             p1.append(l)
#             l = l.left
#         while r.right:
#             p2.append(r)
#             r = r.right
#         while l.val < r.val:
#             t = l.val + r.val
#             if t == k:
#                 return True
#             if t < k:
#                 if l.right:
#                     p1.append(l)
#                     l = l.right
#                     while l.left:
#                         p1.append(l)
#                         l = l.left
#                 else:
#                     v = l.val
#                     while p1:
#                         if l.val > v:
#                             break
#                         l = p1.pop()
#             else:
#                 if r.left:
#                     p2.append(r)
#                     r = r.left
#                     while r.right:
#                         p2.append(r)
#                         r = r.right
#                 else:
#                     v = r.val
#                     while p2:
#                         if r.val < v:
#                             break
#                         r = p2.pop()
#         return False


# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420743/Python-Solution-using-iterators-explained
class Solution:
    def findTarget(self, root: TreeNode, k):
        def get(node, dr):
            if not node: return
            first, last = (node.left, node.right)[::dr]
            yield from get(first, dr)
            yield node.val
            yield from get(last, dr)

        head, tail = get(root, 1), get(root, -1)
        n1, n2 = next(head), next(tail)
        while n1 < n2:
            if n1 + n2 < k:
                n1 = next(head)
            elif n1 + n2 > k:
                n2 = next(tail)
            else:
                return True


tests = [
    [
        [1,0,4,-2,null,3],
        7, True
    ],
    [
        [5,3,6,2,4,null,7], 9, True
    ],
    [
        [5,3,6,2,4,null,7], 28, False
    ],
    [
        [2,1,3], 4, True
    ],
    [
        [2,1,3], 1, False
    ],
    [
        [2,1,3], 3, True
    ]
]

run_functional_tests(Solution().findTarget, convert_test_params_to_trees(tests, indexes=[0]))