"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3903/
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def maxProduct(self, root: TreeNode) -> int:
#
#         MOD = 10**9 + 7
#
#         def tree_sum(root: TreeNode) -> int:
#             result = 0
#             st = []
#             if root:
#                 st.append(root)
#             while st:
#                 node = st.pop()
#                 result += node.val
#                 if node.left:
#                     st.append(node.left)
#                 if node.right:
#                     st.append(node.right)
#             return result
#
#         total_sum = tree_sum(root)
#         max_product = 0
#
#         st = []
#         if root:
#             st.append(root)
#
#         while st:
#             node = st.pop()
#             if node.left:
#                 sum_left = tree_sum(node.left)
#                 sum_rest = total_sum - sum_left
#                 prod = sum_left * sum_rest
#                 max_product = max(max_product, prod)
#                 st.append(node.left)
#             if node.right:
#                 sum_right = tree_sum(node.right)
#                 sum_rest = total_sum - sum_right
#                 prod = sum_right * sum_rest
#                 max_product = max(max_product, prod)
#                 st.append(node.right)
#
#         return max_product % MOD


# Runtime: 356 ms, faster than 62.31% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 80.9 MB, less than 70.90% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# class Solution:
#     def maxProduct(self, root: TreeNode) -> int:
#
#         MOD = 10**9 + 7
#
#         def tree_sum(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             root.sum = root.val + tree_sum(root.left) + tree_sum(root.right)
#             return root.sum
#
#         total_sum = tree_sum(root)
#         max_product = 0
#
#         st = []
#         if root:
#             st.append(root)
#
#         while st:
#             node = st.pop()
#             if node.left:
#                 sum_left = node.left.sum
#                 sum_rest = total_sum - sum_left
#                 prod = sum_left * sum_rest
#                 max_product = max(max_product, prod)
#                 st.append(node.left)
#             if node.right:
#                 sum_right = node.right.sum
#                 sum_rest = total_sum - sum_right
#                 prod = sum_right * sum_rest
#                 max_product = max(max_product, prod)
#                 st.append(node.right)
#
#         return max_product % MOD


# Runtime: 352 ms, faster than 63.43% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 80.9 MB, less than 70.90% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# class Solution:
#     def maxProduct(self, root: TreeNode) -> int:
#
#         MOD = 10**9 + 7
#
#         def tree_sum(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             root.sum = root.val + tree_sum(root.left) + tree_sum(root.right)
#             return root.sum
#
#         total_sum = tree_sum(root)
#         ts2 = total_sum // 2
#         max_product = 0
#         min_dist = total_sum
#
#         st = []
#         if root:
#             st.append(root)
#
#         while st:
#             node = st.pop()
#             if node.left:
#                 sum_left = node.left.sum
#                 sum_rest = total_sum - sum_left
#                 dist = abs(ts2 - sum_left) + abs(ts2 - sum_rest)
#                 if dist < min_dist:
#                     min_dist = dist
#                     prod = sum_left * sum_rest
#                     max_product = prod % MOD
#                 st.append(node.left)
#             if node.right:
#                 sum_right = node.right.sum
#                 sum_rest = total_sum - sum_right
#                 dist = abs(ts2 - sum_right) + abs(ts2 - sum_rest)
#                 if dist < min_dist:
#                     min_dist = dist
#                     prod = sum_right * sum_rest
#                     max_product = prod % MOD
#                 st.append(node.right)
#
#         return max_product


# Runtime: 340 ms, faster than 66.42% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 80.9 MB, less than 70.90% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
class Solution:
    def maxProduct(self, root: TreeNode) -> int:

        MOD = 10**9 + 7

        def tree_sum(root: TreeNode) -> int:
            if not root:
                return 0
            root.sum = root.val + tree_sum(root.left) + tree_sum(root.right)
            return root.sum

        total_sum = tree_sum(root)
        max_product = 0
        min_dist = total_sum

        st = []
        if root:
            st.append(root)

        while st:
            node = st.pop()
            if node.left:
                sum_left = node.left.sum
                sum_rest = total_sum - sum_left
                dist = abs(sum_rest - sum_left)
                if dist < min_dist:
                    min_dist = dist
                    prod = sum_left * sum_rest
                    max_product = prod % MOD
                st.append(node.left)
            if node.right:
                sum_right = node.right.sum
                sum_rest = total_sum - sum_right
                dist = abs(sum_rest - sum_right)
                if dist < min_dist:
                    min_dist = dist
                    prod = sum_right * sum_rest
                    max_product = prod % MOD
                st.append(node.right)

        return max_product


tests = [
    [
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5)),
                 TreeNode(3,
                          TreeNode(6))),
        110
    ],
    [
        TreeNode(1,
                 null,
                 TreeNode(2,
                          TreeNode(3),
                          TreeNode(4,
                                   TreeNode(5),
                                   TreeNode(6)))),
        90
    ],
    [
        TreeNode(2,
                 TreeNode(3,
                          TreeNode(10,
                                   TreeNode(5),
                                   TreeNode(4)),
                          TreeNode(7,
                                   TreeNode(11),
                                   TreeNode(1))),
                 TreeNode(9,
                          TreeNode(8),
                          TreeNode(6))),
        1025
    ],
    [
        TreeNode(1,
                 TreeNode(1)),
        1
    ]
]

run_functional_tests(Solution().maxProduct, tests)