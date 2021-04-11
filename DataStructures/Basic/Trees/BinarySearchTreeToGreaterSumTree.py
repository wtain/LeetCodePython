"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/



Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
Example 3:

Input: root = [1,0,2]
Output: [3,3,2]
Example 4:

Input: root = [3,2,4,1]
Output: [7,9,4,10]


Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.
"""



# Runtime: 32 ms, faster than 67.28% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: 14.2 MB, less than 65.37% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
from Common.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import printTree


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
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

"""
30 
    (36 
        (36 ()
         35 
            (33 ())
        )
    21 
        (26 ()
         15 
            (8 ())))
"""

tests = [
    (
        root1,
        TreeNode(30,
                 TreeNode(36,
                          TreeNode(36),
                          TreeNode(35,
                                   None,
                                   TreeNode(33))),
                 TreeNode(21,
                          TreeNode(26),
                          TreeNode(15,
                                   None,
                                   TreeNode(8))))
    )
]


# printTree(Solution().bstToGst(root1))

run_functional_tests(Solution().bstToGst, tests)