"""
https://leetcode.com/problems/binary-tree-right-side-view/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630/
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


from typing import List


# Runtime: 24 ms, faster than 97.59% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 14.4 MB, less than 21.59% of Python3 online submissions for Binary Tree Right Side View.
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        levels = []

        def rightSideViewImpl(root: TreeNode, level: int):
            if not root:
                return
            nonlocal levels
            if level == len(levels):
                levels.append(root.val)
            rightSideViewImpl(root.right, level+1)
            rightSideViewImpl(root.left, level + 1)

        rightSideViewImpl(root, 0)

        return levels


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)

tests = [
    (root1, [1, 3, 4])
]

run_functional_tests(Solution().rightSideView, tests)


