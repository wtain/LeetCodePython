"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/
https://leetcode.com/problems/trim-a-binary-search-tree/
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.



Example 1:


Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
Example 2:


Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
Example 3:

Input: root = [1], low = 1, high = 2
Output: [1]
Example 4:

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]
Example 5:

Input: root = [1,null,2], low = 2, high = 4
Output: [2]


Constraints:

The number of nodes in the tree in the range [1, 104].
0 <= Node.val <= 104
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 104
"""


from typing import List

# Runtime: 88 ms, faster than 5.30% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 18.4 MB, less than 18.20% of Python3 online submissions for Trim a Binary Search Tree.
from Common.DataTypes.Leetcode import TreeNode


# Runtime: 51 ms, faster than 88.82% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 18 MB, less than 48.91% of Python3 online submissions for Trim a Binary Search Tree.
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


tests = [
    (
        TreeNode(1,
                 TreeNode(0),
                 TreeNode(2)),
        1, 2,
        TreeNode(1,
                 None,
                 TreeNode(2))
    ),

    (
        TreeNode(3,
                 TreeNode(0,
                          None,
                          TreeNode(2,
                                   TreeNode(1))),
                 TreeNode(4)),
        1, 3,
        TreeNode(3,
                 TreeNode(2,
                          TreeNode(1)))
    ),


]


def treesEqual(root1: TreeNode, root2: TreeNode) -> bool:
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    if not treesEqual(root1.left, root2.left):
        return False
    return treesEqual(root1.right, root2.right)


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


for test in tests:
    result = Solution().trimBST(test[0], test[1], test[2])
    if treesEqual(result, test[3]):
        print("PASS")
    else:
        print("FAIL")
        printTree(result)