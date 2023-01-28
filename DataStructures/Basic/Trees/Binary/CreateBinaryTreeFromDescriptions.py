"""
https://leetcode.com/problems/create-binary-tree-from-descriptions/

You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.



Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.


Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
"""
from collections import defaultdict
from typing import List, Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list
from DataStructures.Basic.Trees.Binary.CreateBinaryTreeFromDescriptions_test_case_huge_1 import \
    binary_tree_from_description_test_case_huge_1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# TLE??
# class Solution:
#     def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
#         children = defaultdict(list)
#         has_parent = []
#         for parent, child, isleft in descriptions:
#             children[parent].append((child, isleft == 1))
#             has_parent.append(child)
#         root = [TreeNode(parent) for parent in children if parent not in has_parent][0]
#         level = [root]
#         while level:
#             next_level = []
#             for node in level:
#                 for child, isleft in children[node.val]:
#                     child_node = TreeNode(child)
#                     if isleft:
#                         node.left = child_node
#                     else:
#                         node.right = child_node
#                     next_level.append(child_node)
#             level = next_level
#         return root


# Runtime
# 2171 ms
# Beats
# 97.76%
# Memory
# 31.5 MB
# Beats
# 59.10%
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        has_parent = set()
        for parent, child, isleft in descriptions:
            if child not in nodes:
                child_node = TreeNode(child)
                nodes[child] = child_node
            else:
                child_node = nodes[child]
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if isleft:
                nodes[parent].left = child_node
            else:
                nodes[parent].right = child_node
            has_parent.add(child)
        root = [nodes[parent] for parent in nodes if parent not in has_parent][0]
        return root


tests = [
    # [binary_tree_from_description_test_case_huge_1, None],
    [[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]], build_tree_from_list([50,20,80,15,17,19])],
    [[[1,2,1],[2,3,0],[3,4,1]], build_tree_from_list([1,2,null,null,3,4])],
]

run_functional_tests(Solution().createBinaryTree, tests)
