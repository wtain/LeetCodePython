"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""
from typing import List

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Runtime
# 36 ms
# Beats
# 83.1%
# Memory
# 14.3 MB
# Beats
# 42.87%
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        result = []

        def dfs(node: TreeNode, found_target: bool, distance_to_target: int) -> (bool, int):
            nonlocal result, k, target
            if not node:
                return False, 0
            if found_target:
                if distance_to_target == k:
                    result.append(node.val)
                else:
                    dfs(node.left, True, distance_to_target+1)
                    dfs(node.right, True, distance_to_target+1)
            elif node.val == target.val:
                if k == 0:
                    result.append(node.val)
                dfs(node.left, True, 1)
                dfs(node.right, True, 1)
                return True, 0
            else:
                found_left, dist_left = dfs(node.left, False, 0)
                dist_left += 1
                if found_left:
                    if k - dist_left > 0:
                        dfs(node.right, True, dist_left+1)
                    elif k == dist_left:
                        result.append(node.val)
                    return True, dist_left
                else:
                    found_right, dist_right = dfs(node.right, False, 0)
                    dist_right += 1
                    if found_right:
                        if k - dist_right > 0:
                            dfs(node.left, True, dist_right+1)
                        elif k == dist_right:
                            result.append(node.val)
                        return True, dist_right
            return False, 0

        dfs(root, False, 0)

        return result


tests = [
    [build_tree_from_list([0,1,null,null,2,null,3,null,4]), TreeNode(3), 0, [3]],
    [build_tree_from_list([3,5,1,6,2,0,8,null,null,7,4]), TreeNode(4), 4, [1]],
    [build_tree_from_list([3,5,1,6,2,0,8,null,null,7,4]), TreeNode(2), 2, [6, 3]],
    [build_tree_from_list([3,5,1,6,2,0,8,null,null,7,4]), TreeNode(5), 2, [7,4,1]],
    [build_tree_from_list([1]), TreeNode(1), 3, []],
]

run_functional_tests(Solution().distanceK, tests)
