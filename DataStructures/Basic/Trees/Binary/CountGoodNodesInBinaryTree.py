"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3899/
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.



Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 256 ms, faster than 52.99% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 33.5 MB, less than 45.31% of Python3 online submissions for Count Good Nodes in Binary Tree.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        maxes = []
        st = []
        if root:
            st.append((root, root.val))
        while st:
            node, mx = st.pop()
            if node.val >= mx:
                cnt += 1
            if node.left:
                st.append((node.left, max(node.left.val, mx)))
            if node.right:
                st.append((node.right, max(node.right.val, mx)))
        return cnt


tests = [
    [
        TreeNode(3,
                 TreeNode(1,
                          TreeNode(3)),
                 TreeNode(4,
                          TreeNode(1),
                          TreeNode(5))),
        4
    ],
    [
        TreeNode(3,
                 TreeNode(3,
                          TreeNode(4),
                          TreeNode(2))),
        3
    ],
    [
        TreeNode(1),
        1
    ]
]


run_functional_tests(Solution().goodNodes, tests)