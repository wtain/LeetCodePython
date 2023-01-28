"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.



Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.


Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""
from typing import Optional, List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list



# Runtime
# 1040 ms
# Beats
# 56.75%
# Memory
# 139.7 MB
# Beats
# 24.72%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
#
#         def invert_path(path: str) -> str:
#             return "U" * len(path)
#
#         def dfs(node: TreeNode, path: str) -> (int, str):
#             nonlocal startValue, destValue
#             if not node:
#                 return 0, ""
#             left_count, left_path = dfs(node.left, 'L')
#             right_count, right_path = dfs(node.right, 'R')
#             if left_count == -1 and right_count == 1:
#                 return 2, left_path + right_path
#             if left_count == 1 and right_count == -1:
#                 return 2, right_path + left_path
#             if left_count == 2:
#                 return 2, left_path
#             if right_count == 2:
#                 return 2, right_path
#             if node.val == startValue:
#                 if left_count == 1:
#                     return 2, left_path
#                 if right_count == 1:
#                     return 2, right_path
#                 return -1, invert_path(path)
#             if node.val == destValue:
#                 if left_count == -1:
#                     return 2, invert_path(left_path)
#                 if right_count == -1:
#                     return 2, invert_path(right_path)
#                 return 1, path
#             if left_count == 1:
#                 return left_count, path+left_path
#             if left_count == -1:
#                 return left_count, invert_path(path) + left_path
#             if right_count == 1:
#                 return right_count, path+right_path
#             if right_count == -1:
#                 return right_count, invert_path(path)+right_path
#             return 0, ""
#
#         return dfs(root, "")[1]


# Runtime
# 733 ms
# Beats
# 79.92%
# Memory
# 137.3 MB
# Beats
# 41.29%
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/solutions/1612105/3-steps/
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def find(node: TreeNode, value: int, path: List[str]) -> bool:
            if node.val == value:
                return True
            if node.left and find(node.left, value, path):
                path += 'L'
            elif node.right and find(node.right, value, path):
                path += 'R'
            return path

        source_path, dest_path = [], []
        find(root, startValue, source_path)
        find(root, destValue, dest_path)
        while source_path and dest_path and source_path[-1] == dest_path[-1]:
            source_path.pop()
            dest_path.pop()
        return "".join("U" * len(source_path)) + "".join(reversed(dest_path))


# Map value to tree node
        # Find common ancestor


tests = [
    [build_tree_from_list([1,null,10,12,13,4,6,null,15,null,null,5,11,null,2,14,7,null,8,null,null,null,9,3]), 6, 15, "UURR"],
    [build_tree_from_list([1,2]), 2, 1, "U"],
    [build_tree_from_list([5,1,2,3,null,6,4]), 3, 6, "UURL"],
    [build_tree_from_list([2,1]), 2, 1, "L"],
]

run_functional_tests(Solution().getDirections, tests)
