"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 56 ms, faster than 32.08% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 17.1 MB, less than 15.83% of Python3 online submissions for Average of Levels in Binary Tree.
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        levels = []

        def walkLevels(root: TreeNode, level: int):
            if not root:
                return
            nonlocal levels
            if len(levels) <= level:
                levels.append([root.val, 1])
            else:
                levels[level][0] += root.val
                levels[level][1] += 1
            walkLevels(root.left, level + 1)
            walkLevels(root.right, level + 1)

        walkLevels(root, 0)

        return [s / c for s, c in levels]


root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

tests = [
    (root1, [3, 14.5, 11])
]

for test in tests:
    result = Solution().averageOfLevels(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))