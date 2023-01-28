"""
https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.



Example 1:


Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
Output: [[2,2],[4,6],[15,-1]]
Explanation: We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].
Example 2:


Input: root = [4,null,9], queries = [3]
Output: [[-1,4]]
Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].


Constraints:

The number of nodes in the tree is in the range [2, 105].
1 <= Node.val <= 106
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 106
"""
import bisect
from typing import Optional, List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list
from DataStructures.Basic.Trees.Binary.ClosestNodesQueriesInABinarySearchTree_test_huge_data import queries, \
    test_huge_data_list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
#
#         def search_low(query: int) -> (int, int):
#             nonlocal root
#             node_left, node_right = root, root
#
#         response = []
#
#         for query in queries:
#             a, b = search_low(query)
#             response.append([a, b])
#
#         return response

# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/solutions/2831836/bst-search-variation-o-1-space-array-approach-o-nlogn-for-sure/
# TLE/Crash
# class Solution:
#     def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
#
#         def search_low(query: int) -> (int, int):
#             nonlocal root
#             node = root
#             lb, ub = float('-inf'), float('inf')
#             while node:
#                 if node.val > query:
#                     ub = min(ub, node.val)
#                     node = node.left
#                 elif node.val < query:
#                     lb = max(lb, node.val)
#                     node = node.right
#                 else:
#                     return node.val, node.val
#             return lb if lb != float('-inf') else -1, ub if ub != float('inf') else -1
#
#         response = []
#
#         for query in queries:
#             a, b = search_low(query)
#             response.append([a, b])
#
#         return response


# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/solutions/2831836/bst-search-variation-o-1-space-array-approach-o-nlogn-for-sure/
# TLE/Crash
# class Solution:
#     def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
#
#         def build_array(root: TreeNode) -> List[int]:
#             if not root:
#                 return []
#             left_arr = build_array(root.left)
#             right_arr = build_array(root.right)
#             return left_arr + [root.val] + right_arr
#
#         array = build_array(root)
#         n = len(array)
#         result = []
#         for query in queries:
#             l, h = 0, n-1
#             lb, rb = float('-inf'), float('inf')
#             while l <= h:
#                 mid = (l + h) // 2
#                 if array[mid] == query:
#                     lb, rb = query, query
#                     break
#                 elif array[mid] < query:
#                     lb = max(lb, array[mid])
#                     l = mid + 1
#                 else:
#                     rb = min(rb, array[mid])
#                     h = mid - 1
#             result.append([lb if lb != float('-inf') else -1, rb if rb != float('inf') else -1])
#         return result


# Runtime
# 1482 ms
# Beats
# 89.72%
# Memory
# 156.7 MB
# Beats
# 37.22%
# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/solutions/2835174/python-3-14-lines-dfs-w-example-t-m-1140ms-15-4mb/
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        def build_array(root: TreeNode, array: List[int]):
            if not root:
                return
            build_array(root.left, array)
            array.append(root.val)
            build_array(root.right, array)

        array = []
        build_array(root, array)
        n = len(array)
        result = []
        for query in queries:
            index = bisect.bisect_left(array, query)
            if index == n:
                result.append([array[-1], -1])
            elif array[index] == query:
                result.append([query, query])
            elif index == 0:
                result.append([-1, array[0]])
            else:
                result.append([array[index-1], array[index]])
        return result


tests = [
    # [build_tree_from_list(test_huge_data_list), queries, []],
    [build_tree_from_list([6,2,13,1,4,9,15,null,null,null,null,null,null,14]), [2,5,16], [[2,2],[4,6],[15,-1]]],
    [build_tree_from_list([4,null,9]), [3], [[-1,4]]],
]

run_functional_tests(Solution().closestNodes, tests)
