"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime: 92 ms, faster than 26.96% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.1 MB, less than 77.03% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def sortedArrayToBSTImpl(nums: List[int], l, r: int):
            cnt = r - l
            if cnt == 0:
                return None
            if cnt == 1:
                return TreeNode(nums[l])
            m = l + cnt // 2
            return TreeNode(nums[m], sortedArrayToBSTImpl(nums, l, m), sortedArrayToBSTImpl(nums, m+1, r))

        return sortedArrayToBSTImpl(nums, 0, len(nums))


def printTree(root: TreeNode):

    def printTreeImpl(root: TreeNode):
        if root is None:
            return
        printTreeImpl(root.left)
        print(root.val, flush=True, sep=' ', end=' ')
        printTreeImpl(root.right)

    printTreeImpl(root)
    print()


"""
      0
     / \
   -3   9
   /   /
 -10  5
"""
printTree(Solution().sortedArrayToBST([-10,-3,0,5,9]))


