"""
https://leetcode.com/problems/sum-of-left-leaves/
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
from Common.DataTypes.Leetcode import TreeNode

"""
Runtime: 24 ms, faster than 98.02% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.5 MB, less than 21.20% of Python3 online submissions for Sum of Left Leaves.
"""
class Solution:

    @staticmethod
    def isLeave(root: TreeNode):
        return root.left is None and root.right is None

    def sumOfLeftLeavesImpl(self, root: TreeNode, isLeft: bool) -> int:
        if Solution.isLeave(root):
            return root.val if isLeft else 0
        sumleft = sumright = 0
        if root.left:
            sumleft = self.sumOfLeftLeavesImpl(root.left, True)
        if root.right:
            sumright = self.sumOfLeftLeavesImpl(root.right, False)
        return sumleft + sumright

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.sumOfLeftLeavesImpl(root, False)


t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

print(Solution().sumOfLeftLeaves(t1))  # 24

