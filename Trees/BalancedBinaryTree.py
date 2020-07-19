"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime: 40 ms, faster than 99.16% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.8 MB, less than 5.77% of Python3 online submissions for Balanced Binary Tree.
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBalancedImpl(root: TreeNode) -> (bool, int):
            if root is None:
                return True, 0
            lb, ll = isBalancedImpl(root.left)
            if not lb:
                return False, ll+1
            rb, rl = isBalancedImpl(root.right)
            if not rb:
                return False, rl + 1
            return abs(rl - ll) <= 1, max(ll, rl) + 1

        return isBalancedImpl(root)[0]


tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

print(Solution().isBalanced(tree1))  # True


tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(2)

tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(3)

tree2.left.left.left = TreeNode(4)
tree2.left.left.right = TreeNode(4)

print(Solution().isBalanced(tree2))  # False

