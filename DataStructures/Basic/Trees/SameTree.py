"""
https://leetcode.com/problems/same-tree/
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
from Common.DataTypes.Leetcode import TreeNode

"""
Runtime: 40 ms, faster than 23.85% of Python3 online submissions for Same Tree.
Memory Usage: 14 MB, less than 5.84% of Python3 online submissions for Same Tree.
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

print(Solution().isSameTree(tree1, tree2))  # True


tree1 = TreeNode(1)
tree1.left = TreeNode(2)

tree2 = TreeNode(1)
tree2.right = TreeNode(2)

print(Solution().isSameTree(tree1, tree2))  # False


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(1)

tree2 = TreeNode(1)
tree2.left = TreeNode(1)
tree2.right = TreeNode(2)

print(Solution().isSameTree(tree1, tree2))  # False