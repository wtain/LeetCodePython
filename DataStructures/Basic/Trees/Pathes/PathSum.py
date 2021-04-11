"""
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 40 ms, faster than 89.58% of Python3 online submissions for Path Sum.
Memory Usage: 15.4 MB, less than 98.89% of Python3 online submissions for Path Sum.
"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        if self.hasPathSum(root.left, sum - root.val):
            return True
        return self.hasPathSum(root.right, sum - root.val)


t1 = TreeNode(5)
t1.left = TreeNode(4)
t1.right = TreeNode(8)

t1.left.left = TreeNode(11)
t1.left.left.left = TreeNode(7)
t1.left.left.right = TreeNode(2)

t1.right.left = TreeNode(13)
t1.right.right = TreeNode(4)

t1.right.right.right = TreeNode(1)

tests = [
    (t1, 22, True)
]

run_functional_tests(Solution().hasPathSum, tests)
