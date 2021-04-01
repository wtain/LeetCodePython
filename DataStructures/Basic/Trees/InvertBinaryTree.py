"""
https://leetcode.com/problems/invert-binary-tree/
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Runtime: 20 ms, faster than 98.67% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.8 MB, less than 51.05% of Python3 online submissions for Invert Binary Tree.
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        toVisit: List[TreeNode] = [root]
        while len(toVisit) > 0:
            nextLevel: List[TreeNode] = []
            for n in toVisit:
                tmp = n.right
                n.right = n.left
                n.left = tmp
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            toVisit = nextLevel
        return root


def printTree(root: TreeNode):
    if not root:
        return
    toVisit: List[TreeNode] = [root]
    while len(toVisit) > 0:
        nextLevel: List[TreeNode] = []
        for n in toVisit:
            if n.left:
                nextLevel.append(n.left)
            if n.right:
                nextLevel.append(n.right)
            print(n.val, flush=True, sep=' ', end=' ')
        print()
        toVisit = nextLevel


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

printTree(root)
printTree(Solution().invertTree(root))
printTree(Solution().invertTree(None))
