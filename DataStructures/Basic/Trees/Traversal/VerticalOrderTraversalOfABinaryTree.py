"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3621/

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right. Each report is a list of all nodes at a given x-coordinate. The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
The node with value 9 occurs at position (-1, -1).
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
The node with value 20 occurs at position (1, -1).
The node with value 7 occurs at position (2, -2).
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""


from typing import List, Dict

from sortedcontainers import SortedDict


# Runtime: 36 ms, faster than 54.10% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
# Memory Usage: 14.5 MB, less than 65.37% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


class Solution:

    def verticalTraversalImpl(self, cache: Dict[int, Dict[int, List[int]]], root: TreeNode, x: int, y: int):
        if not root:
            return
        if not cache.get(x):
            cache[x] = {}
        if not cache[x].get(y):
            cache[x][y] = []
        cache[x][y].append(root.val)
        self.verticalTraversalImpl(cache, root.left, x - 1, y + 1)
        self.verticalTraversalImpl(cache, root.right, x + 1, y + 1)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        cache: SortedDict[int, SortedDict[int, List[int]]] = {}
        self.verticalTraversalImpl(cache, root, 0, 0)

        result: List[List[int]] = []

        for d in sorted(cache):
            result.append([])
            for s in sorted(cache[d]):
                for v in sorted(cache[d][s]):
                    result[-1].append(v)

        return result

# [0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right = TreeNode(3)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)

tests = [
    (root1, [[9],[3,15],[20],[7]]),
    (root2, [[4],[2],[1,5,6],[3],[7]])
]


run_functional_tests(Solution().verticalTraversal, tests)