"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/
https://leetcode.com/problems/convert-bst-to-greater-tree/
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 92 ms, faster than 24.06% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 18.8 MB, less than 5.07% of Python3 online submissions for Convert BST to Greater Tree.
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def convertBSTImpl(root: TreeNode, v: int) -> (TreeNode, int):
            if not root:
                return None, 0
            newRight, sumRight = convertBSTImpl(root.right, v)
            newRoot = TreeNode(root.val + sumRight + v)
            newLeft, sumLeft = convertBSTImpl(root.left, newRoot.val)
            newRoot.left = newLeft
            newRoot.right = newRight
            return newRoot, sumLeft + root.val + sumRight

        return convertBSTImpl(root, 0)[0]


root1 = TreeNode(4)
root1.left = TreeNode(1)
root1.right = TreeNode(6)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(2)
root1.left.right.right = TreeNode(3)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(7)
root1.right.right.right = TreeNode(8)

def printTree(root: TreeNode):

    def printTreeImpl(root: TreeNode):
        if root is None:
            return
        printTreeImpl(root.left)
        print(root.val, flush=True, sep=' ', end=' ')
        printTreeImpl(root.right)

    printTreeImpl(root)
    print()


printTree(Solution().convertBST(root1))