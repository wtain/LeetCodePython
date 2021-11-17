"""
https://leetcode.com/problems/validate-binary-tree-nodes/

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.



Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:


Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false


Constraints:

1 <= n <= 104
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2220 ms, faster than 5.82% of Python3 online submissions for Validate Binary Tree Nodes.
# Memory Usage: 16.2 MB, less than 85.01% of Python3 online submissions for Validate Binary Tree Nodes.
# class Solution:
#     def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
#         n = len(leftChild)
#         parent = [-1] * n
#         root = list(range(n))
#
#         def get_root(i: int) -> int:
#             while root[i] != i:
#                 i = root[i]
#             return i
#
#         for i in range(n):
#             l, r = leftChild[i], rightChild[i]
#             for c in [l, r]:
#                 if c != -1:
#                     if parent[c] != -1:
#                         return False
#                     parent[c] = i
#                     nr = get_root(i)
#                     if root[c] == nr:
#                         return False
#                     root[c] = nr
#
#         root = [get_root(root[i]) for i in range(n)]
#
#         return min(root) == max(root)


# Runtime: 312 ms, faster than 75.13% of Python3 online submissions for Validate Binary Tree Nodes.
# Memory Usage: 15.8 MB, less than 99.12% of Python3 online submissions for Validate Binary Tree Nodes.
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        n = len(leftChild)
        parent = [-1] * n

        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            for c in [l, r]:
                if c != -1:
                    if parent[c] != -1:
                        return False
                    parent[c] = i

        root = -1
        for i in range(n):
            if parent[i] == -1:
                if root != -1:
                    return False
                root = i
        if root == -1:
            return False

        level = [root]
        cnt = 0
        while level:
            next_level = []
            for c in level:
                cnt += 1
                if leftChild[c] != -1:
                    next_level.append(leftChild[c])
                if rightChild[c] != -1:
                    next_level.append(rightChild[c])
            level = next_level

        return cnt == n


tests = [
    [4, [1,-1,3,-1], [2,-1,-1,-1], True],
    [4, [1,-1,3,-1], [2,3,-1,-1], False],
    [2, [1,0], [-1,-1], False],
    [6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1], False],
    [4, [3,-1,1,-1], [-1,-1,0,-1], True],
    [4, [1,0,3,-1], [-1,-1,-1,-1], False]
]

run_functional_tests(Solution().validateBinaryTreeNodes, tests)
