"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3689/
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:


Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].



Example 1:


Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
Example 2:


Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.
Example 3:


Input: root = [1,2,3], voyage = [1,2,3]
Output: []
Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.


Constraints:

The number of nodes in the tree is n.
n == voyage.length
1 <= n <= 100
1 <= Node.val, voyage[i] <= n
All the values in the tree are unique.
All the values in voyage are unique.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


## WRONG???
# class Solution:
# 
#     def __init__(self):
#         self.mapping = None
# 
#     def flipMatchVoyage(self, root: TreeNode, voyage: List[int], start: int = 0) -> List[int]:
# 
#         if not self.mapping:
#             self.mapping = {v: i for i, v in enumerate(voyage)}
# 
#         if not root and len(voyage) > 0:
#             return [-1]
#         if root and len(voyage) == 0:
#             return [-1]
#         if root.val != voyage[0]:
#             return [-1]
# 
#         if root.left and root.right:
#             if voyage[1] == root.left.val:
#                 idx = self.mapping[root.right.val] - start
#                 res1 = self.flipMatchVoyage(root.left, voyage[1:idx], start+1)
#                 res2 = self.flipMatchVoyage(root.right, voyage[idx:], start+idx)
#                 if res1 == [-1] or res2 == [-1]:
#                     return [-1]
#                 return res1 + res2
#             elif voyage[1] == root.right.val:
#                 idx = self.mapping[root.left.val] - start
#                 res1 = self.flipMatchVoyage(root.right, voyage[1:idx], start+1)
#                 res2 = self.flipMatchVoyage(root.left, voyage[idx:], start+idx)
#                 if res1 == [-1] or res2 == [-1]:
#                     return [-1]
#                 return [root.val] + res1 + res2
#             else:
#                 return [-1]
#         elif root.left:
#             return self.flipMatchVoyage(root.left, voyage[1:])
#         elif root.right:
#             return self.flipMatchVoyage(root.right, voyage[1:])
#         else:
#             return []


# Runtime: 32 ms, faster than 84.18% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
# Memory Usage: 14.1 MB, less than 89.27% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
class Solution:

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        result = []
        i = 0
        
        def impl(node: TreeNode):
            nonlocal i, result
            if node:
                if node.val != voyage[i]:
                    result = [-1]
                    return 
                i += 1
                if i < len(voyage) and node.left and node.left.val != voyage[i]:
                    result.append(node.val)
                    impl(node.right)
                    impl(node.left)
                else:
                    impl(node.left)
                    impl(node.right)

        impl(root)
        if result and result[0] == -1:
            result = [-1]
        return result


# Runtime: 32 ms, faster than 84.53% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
# Memory Usage: 14.2 MB, less than 88.95% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
# class Solution(object):
#     def flipMatchVoyage(self, root, voyage):
#         self.flipped = []
#         self.i = 0
#
#         def dfs(node):
#             if node:
#                 if node.val != voyage[self.i]:
#                     self.flipped = [-1]
#                     return
#                 self.i += 1
#                 if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
#                     self.flipped.append(node.val)
#                     dfs(node.right)
#                     dfs(node.left)
#                 else:
#                     dfs(node.left)
#                     dfs(node.right)
#
#         dfs(root)
#         if self.flipped and self.flipped[0] == -1:
#             self.flipped = [-1]
#         return self.flipped


tests = [
    (
        (
            TreeNode(1,
                     TreeNode(5,
                              TreeNode(7),
                              TreeNode(2)),
                     TreeNode(6,
                              TreeNode(4),
                              TreeNode(3)))
        ),
        [1,5,2,6,3,4,7],
        [-1]
    ),

    (
        TreeNode(2,
                 TreeNode(1,
                          TreeNode(4),
                          TreeNode(3))),
        [2,1,3,4],
        [1]
     ),

    (TreeNode(1, TreeNode(2)), [2, 1], [-1]),
    (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 3, 2], [1]),
    (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3], [])
]

run_functional_tests(Solution().flipMatchVoyage, tests)