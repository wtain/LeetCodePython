"""
https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.

"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime: 32 ms, faster than 81.75% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.1 MB, less than 21.87% of Python3 online submissions for Symmetric Tree.
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        l: List[TreeNode] = []
        r: List[TreeNode] = []

        l.append(root.left)
        r.append(root.right)

        while len(l) > 0 and len(r) > 0:
            li = l.pop()
            ri = r.pop()
            if li is None and ri is None:
                continue
            if li is None or ri is None:
                return False
            if li.val != ri.val:
                return False
            l.append(li.left)
            l.append(li.right)

            r.append(ri.right)
            r.append(ri.left)

        return len(l) == 0 and len(r) == 0


tree1 = TreeNode(1)

tree1.left = TreeNode(2)
tree1.right = TreeNode(2)

tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(4)

tree1.right.left = TreeNode(4)
tree1.right.right = TreeNode(3)

print(Solution().isSymmetric(tree1))  # True

tree2 = TreeNode(1)

tree2.left = TreeNode(2)
tree2.right = TreeNode(2)

tree2.left.right = TreeNode(3)

tree2.right.right = TreeNode(3)

print(Solution().isSymmetric(tree2))  # False
