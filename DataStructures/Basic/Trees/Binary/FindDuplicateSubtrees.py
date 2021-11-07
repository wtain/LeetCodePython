"""
https://leetcode.com/problems/find-duplicate-subtrees/

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.



Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List

from Common.Constants import null
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.ResultComparators import compareSets
from Common.TreeUtils import build_tree_from_list


# WRONG
# class Solution:
#     def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
#         result = []
#         seen = set()
#
#         def trees_equal(node1: TreeNode, node2: TreeNode) -> bool:
#             if not node1 and not node2:
#                 return True
#             if not node1 or not node2:
#                 return False
#             if node1.val != node2.val:
#                 return False
#             return trees_equal(node1.left, node2.left) and trees_equal(node1.right, node2.right)
#
#         def find_subtree(root: TreeNode, code1: int, subtreeroot: TreeNode, code2: int) -> bool:
#             if not root or not subtreeroot:
#                 return False
#             if code1 != code2 and trees_equal(root, subtreeroot):
#                 return True
#             return find_subtree(root.left, 2*code1, subtreeroot, code2) or find_subtree(root.right, 2*code1+1, subtreeroot, code2)
#
#         def impl(node: TreeNode, code: int):
#             nonlocal result, root
#             if not node:
#                 return
#             left_code, right_code = 2*code, 2*code+1
#             if left_code not in seen and find_subtree(root, 0, node.left, left_code):
#                 result.append(node.left)
#                 seen.add(left_code)
#             if right_code not in seen and find_subtree(root, 0, node.right, right_code):
#                 result.append(node.right)
#                 seen.add(right_code)
#             impl(node.left, 2*code)
#             impl(node.right, 2*code+1)
#
#         impl(root, 0)
#         return result


# WRONG
# class Solution:
#     def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
#         result = []
#         seen = defaultdict(list)
#         m, mod = 17, 1e7+1
#
#         def trees_equal(node1: TreeNode, node2: TreeNode) -> bool:
#             if not node1 and not node2:
#                 return True
#             if not node1 or not node2:
#                 return False
#             if node1.val != node2.val:
#                 return False
#             return trees_equal(node1.left, node2.left) and trees_equal(node1.right, node2.right)
#
#         def impl(node: TreeNode, parent_hash: int):
#             nonlocal m, mod, seen
#             if not node:
#                 return
#             hash = (parent_hash * m + node.val+200) % mod
#             seen[hash].append(node)
#             impl(node.left, hash)
#             impl(node.right, hash)
#
#         impl(root, 0)
#
#         for eq_list in seen.values():
#             k = len(eq_list)
#             for i in range(k):
#                 found = False
#                 for j in range(i+1, k):
#                     if trees_equal(eq_list[i], eq_list[j]):
#                         result.append(eq_list[i])
#                         found = True
#                         break
#                 if found:
#                     break
#
#         return result


# WRONG
# class Solution:
#     def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
#         result = []
#         seen = defaultdict(list)
#         m, mod = 17, 1e7+1
#
#         def trees_equal(node1: TreeNode, node2: TreeNode) -> bool:
#             if not node1 and not node2:
#                 return True
#             if not node1 or not node2:
#                 return False
#             if node1.val != node2.val:
#                 return False
#             return trees_equal(node1.left, node2.left) and trees_equal(node1.right, node2.right)
#
#         def calc_hashes(node: TreeNode) -> int:
#             nonlocal m, mod, seen
#             if not node:
#                 return 0
#             lh = calc_hashes(node.left)
#             rh = calc_hashes(node.right)
#             h = ((node.val + 200) * m + lh + rh) % mod
#             seen[h].append(node)
#             return h
#
#         calc_hashes(root)
#
#         for eq_list in seen.values():
#             k = len(eq_list)
#             for i in range(k):
#                 found = False
#                 for j in range(i+1, k):
#                     if trees_equal(eq_list[i], eq_list[j]):
#                         result.append(eq_list[i])
#                         found = True
#                         break
#                 if found:
#                     break
#
#         return result


# Runtime: 147 ms, faster than 12.95% of Python3 online submissions for Find Duplicate Subtrees.
# Memory Usage: 21.9 MB, less than 66.47% of Python3 online submissions for Find Duplicate Subtrees.
# https://leetcode.com/problems/find-duplicate-subtrees/discuss/1545834/Java-or-beats-97-HashMap-T%3AO(N)-S%3AO(NlogN)
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        result = []
        seen = dict()

        def post_order(node: TreeNode) -> str:
            nonlocal result, seen
            if not node:
                return ""
            left, right = post_order(node.left), post_order(node.right)
            code = ""
            if left:
                code += left + "L"
            if right:
                code += right + "R"
            code += str(node.val) + "C"
            if code not in seen:
                seen[code] = False
            elif not seen[code]:
                seen[code] = True
                result.append(node)
            return code

        post_order(root)

        return result



tests = [
    [
        build_tree_from_list([1,2,3,4,null,2,4,null,null,4]),
        [
            build_tree_from_list([2,4]),
            build_tree_from_list([4]),
        ]
    ],
    [
        build_tree_from_list([2,1,1]),
        [
            build_tree_from_list([1])
        ]
    ],
    [
        build_tree_from_list([2,2,2,3,null,3,null]),
        [
            build_tree_from_list([2,3]),
            build_tree_from_list([3])
        ]
    ],
    [
        build_tree_from_list([1,5,8,9,7,7,8,1,4,8,1,9,0,8,7,1,7,4,2,9,8,2,4,null,null,9,null,null,null,6,0,9,4,1,0,1,8,9,0,1,8,9,1,0,9,6,2,5,null,2,3,0,2,4,8,8,8,5,0,0,9,4,9,1,null,0,7,2,2,3,null,6,1,0,8,9,9,9,4,8,4,3,4,4,0,null,null,8,3,8,null,null,0,null,0,4,9,1,2,null,4,4,0,4,3,5,5,7,4,1,6,null,1,0,null,null,null,2,8,7,7,null,null,0,2,5,5,9,3,3,null,7,6,6,7,9,8,1,7,7,7,2,6,null,7,null,4,6,4,6,null,null,9,1,null,null,null,5,5,5,4,2,2,8,5,1,1,3,1,3,7,null,2,null,9,1,4,4,7,7,null,1,5,6,2,7,3,null,9,1,null,2,4,4,8,null,null,7,null,6,null,7,4,3,5,8,4,8,5,null,null,8,null,null,null,4,4,null,null,null,null,8,3,5,5,null,null,null,1,2,0,null,null,9,3,null,8,3,7,1,8,9,0,1,8,2,null,4,null,null,8,null,null,null,null,2,null,4,8,5,5,3,1,null,null,6,null,1,null,null,6,null,null,null,null,7,3,null,null,null,8,6,4,null,6,9,0,7,8,null,null,0,6,7,null,null,0,0,7,2,3,2,null,0,2,3,null,0,1,7,9,0,7,null,null,null,null,5,8,2,6,3,2,0,4,null,null,0,9,1,1,1,null,1,3,null,7,9,1,3,3,8,null,null,null,null,6,null,null,null,null,9,8,1,3,8,3,0,6,null,null,8,5,6,5,2,1,null,5,null,7,0,0,null,9,3,9,null,3,0,0,9,1,7,0,2,null,6,8,5,null,null,null,null,null,7,null,2,5,null,null,9,null,null,null,null,null,null,null,null,null,null,null,4,1,null,3,6,6,2,5,5,9,null,null,7,8,null,null,2,7,3,7,2,5,null,1,3,4,null,null,8,3,6,9,null,1,null,null,null,null,9,7,5,2,null,5,null,6,4,5,null,1,2,0,6,null,1,6,null,null,5,null,7,8,4,7,8,6,4,null,5,6,7,9,1,0,4,null,null,null,6,4,8,4,5,null,0,4,4,0,1,7,1,null,1,null,3,6,null,null,null,null,8,null,5,0,7,5,null,null,5,8,null,null,3,null,null,8,null,2,4,null,null,null,null,null,null,null,9,null,9,null,9,null,null,null,null,7,1,null,null,2,null,null,5,5,5,5,6,4,null,null,1,6,4,0,null,0,6,3,0,null,5,5,null,null,null,null,2,null,3,6,null,3,0,5,0,1,0,3,4,9,9,2,7,3,8,6,9,null,5,8,null,null,null,null,9,8,0,7,null,null,8,8,6,6,0,2,7,4,2,3,8,6,4,null,8,null,null,null,2,0,null,1,3,5,4,2,2,5,8,8,null,3,0,null,1,6,0,null,null,9,null,2,null,6,8,2,null,null,5,null,null,null,9,6,6,4,2,0,null,null,1,null,0,null,null,null,6,6,null,null,null,4,7,9,null,0,1,null,null,9,null,null,null,4,null,8,null,null,null,null,null,null,4,null,6,null,3,null,null,5,1,2,5,null,0,7,8,null,7,null,null,4,null,4,4,null,2,null,6,null,null,null,7,null,null,null,null,6,4,null,6,null,6,9,null,null,null,9,6,null,9,null,3,null,2,null,7,7,null,null,0,null,6,3,null,null,null,null,null,null,1,null,null,null,6,9,7,null,7,null,9,3,3,null,null,null,null,4,null,null,3,null,null,null,3,9,null,0,3,1,9,6,7,9,4,8,null,null,6,null,1,3,7,null,null,null,3,null,2,null,8,1,1,null,null,6,null,7,3,5,null,6,3,4,null,null,5,7,1,null,null,6,4,6,null,null,null,null,5,7,0,7,0,null,5,8,5,5,4,5,null,null,null,null,null,null,1,7,null,null,7,null,9,9,6,4,null,null,3,2,1,null,0,null,0,6,null,null,null,1,5,null,null,null,8,null,null,null,null,3,4,8,null,null,9,6,4,null,null,null,null,8,9,null,1,null,null,null,7,null,null,null,null,null,9,null,null,null,4,1,6,7,0,null,null,null,7,null,null,8,null,null,null,null,null,null,null,4,null,9,null,null,null,null,3,0,6,null,5,null,9,9,null,null,4,3,4,null,null,null,null,8,null,5,null,null,null,null,5,2,null,null,null,null,null,null,null,2,null,null,2,1,8,5,null,0,null,0,3,2,4,5,null,null,null,null,null,7,null,null,0,null,0,null,null,null,0,3,9,null,null,null,null,5,null,null,0,5,0,0,null,9,null,null,null,null,null,null,null,null,8,null,9,3,5,9,0,5,9,null,null,9,4,null,0,2,0,null,null,7,null,7,null,5,7,8,7,null,null,null,3,0,3,null,null,null,null,null,4,5,null,null,2,3,null,2,null,null,7,null,null,9,null,null,9,7,1,null,null,1,6,1,8,null,null,5,null,null,3,7,9,6,null,null,null,null,1,null,null,null,3,7,3,2,3,3,null,1,null,null,null,1,null,null,4,3,4,8,7,null,0,3,0,null,1,1,null,null,null,null,null,5,null,6,0,null,3,1,null,6,null,null,4,0,1,null,6,1,null,null,9,6,4,9,0,8,9,3,3,6,null,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,8,5,8,3,5,4,null,6,null,0,null,null,6,null,4,3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,7,3,null,null,1,null,2,4,null,null,null,6,null,null,null,6,null,5,null,null,null,null,1,null,null,3,null,1,null,7,1,null,null,7,1,3,4,8,null,null,null,null,null,4,null,null,4,null,null,null,7,null,6,null,null,1,null,null,null,7,3,3,null,null,null,null,3,0,null,null,4,null,null,null,null,null,null,null,null,null,null,8,null,null,9,null,null,6,6,5,2,null,8,3,8,null,null,null,null,6,7,0,null,null,null,null,1,1,5,null,0,5,null,5,null,null,null,1,2,null,2,9,1,null,2,4,1,null,null,null,1,8,4,4,5,2,null,null,6,4,7,5,2,9,null,4,null,null,null,null,null,3,null,null,5,9,null,null,null,null,9,null,9,null,null,null,2,null,1,9,null,null,null,null,null,1,9,3,null,null,1,9,null,5,2,1,0,null,null,1,9,8,4,7,null,null,5,7,null,null,null,null,1,2,8,null,6,0,null,null,null,null,0,null,null,null,6,null,2,3,0,9,null,null,1,4,6,null,8,null,null,5,null,3,0,null,6,null,null,null,null,null,2,null,null,null,null,null,null,2,5,8,6,9,null,null,null,8,null,null,9,6,null,null,null,null,3,null,null,null,null,9,null,null,2,null,null,null,null,null,null,8,8,null,null,null,null,null,9,null,6,null,2,5,null,null,1,2,null,4,null,null,4,null,null,3,5,null,3,3,null,null,1,null,null,null,null,4,null,2,3,null,4,5,3,null,7,null,null,null,7,6,null,null,1,3,null,4,9,8,null,null,0,null,3,4,null,8,null,1,null,null,2,2,null,null,4,null,null,null,3,null,null,2,null,null,null,4,null,5,null,null,null,null,2,null,5,null,null,null,null,null,null,2,7,5,null,6,null,null,null,null,2,null,0,null,3,null,1,null,9,4,null,3,null,null,null,null,null,null,null,5,5,7,null,null,1,null,4,6,null,null,null,2,null,5,9,0,6,2,null,null,null,null,null,null,null,null,null,null,null,null,5,null,7,null,2,9,null,null,1,null,null,null,1,6,null,6,null,null,0,8,null,4,null,null,null,null,4,null,null,0,null,6,0,null,null,null,4,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,0,5,4,2,6,4,5,3,4,null,null,5,null,null,null,null,4,null,null,3,6,2,0,null,6,6,null,null,null,null,0,6,null,null,null,3,9,4,null,null,null,null,null,0,null,null,6,7,0,null,9,2,null,3,3,null,null,8,null,3,null,null,null,8,5,3,null,2,4,null,9,6,9,null,null,null,null,6,null,6,null,5,3,null,null,null,null,4,null,null,null,9,0,9,7,1,1,null,1,null,1,6,null,5,null,6,null,null,1,null,null,null,null,null,null,5,null,null,null,null,null,3,null,6,1,null,0,2,null,null,0,null,null,0,null,null,null,null,null,3,null,null,8,null,null,5,3,3,null,null,null,null,null,null,null,3,null,null,0,8,7,null,null,8,1,null,null,null,null,null,null,7,null,null,null,null,null,null,null,null,null,null,null,5,2,null,2,6,null,null,null,null,null,null,null,1,5,0,null,null,2,null,7,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,null,8,null,null,null,null,3,null,null,4,null,null,2,null,null,null,null,0,3,null,null,null,null,null,7,null,8,null,null,null,null,8,5,null,3,4,null,null,null,8,null,null,null,null,null,null,null,null,null,3,7,null,null,null,4,0,3,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,8,null,null,null,null,null,2,null,null,null,null,null,null,null,null,null,0,null,null,null,2,null,null,null,8,2,null,null,null,null,null,null,null,8,null,null,null,null,null,null,null,null,null,null,2,null,null,null,2,5,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,8,null,null,null,null,null,null,null,null,null,null,0,5]),
        map(build_tree_from_list, [[9],[8,1],[6,null,8],[9,2],[4,6],[8],[5],[8,null,6],[2],[4,7],[3],[1],[6],[7],[1,null,1],[9,null,9],[4,1],[2,null,4],[0,8],[1,7],[0,5],[9,null,2],[3,null,7],[9,0],[4],[3,3],[1,1],[4,null,6],[3,null,5,null,3],[0,null,1],[2,null,1],[5,8],[6,8],[6,null,5],[5,null,3],[1,0],[3,6],[1,2],[0,null,4],[1,null,3],[0,null,5],[1,null,5],[0],[6,null,6],[5,6],[7,6],[2,4],[4,null,0],[3,8],[1,4],[8,6],[6,null,0],[2,null,8],[0,2]])
    ]
]

run_functional_tests(Solution().findDuplicateSubtrees, tests)
