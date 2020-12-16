"""
https://leetcode.com/problems/validate-binary-search-tree/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3568/
Runtime: 44 ms, faster than 65.88% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.3 MB, less than 53.23% of Python3 online submissions for Validate Binary Search Tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTImpl(root: TreeNode, vmin, vmax):
            if root is None:
                return True
            if vmin is not None and root.val <= vmin:
                return False
            if vmax is not None and root.val >= vmax:
                return False
            return isValidBSTImpl(root.left, vmin, root.val) and isValidBSTImpl(root.right, root.val, vmax)
        return isValidBSTImpl(root, None, None)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(Solution().isValidBST(root1))  # true

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(Solution().isValidBST(root2))  # false
