"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3827/

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

from typing import List

from Common.DataTypes.Leetcode import TreeNode
from Common.TreeUtils import printTree

"""
Runtime: 92 ms, faster than 26.96% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.1 MB, less than 77.03% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Runtime: 56 ms, faster than 88.65% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.7 MB, less than 59.53% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
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


"""
      0
     / \
   -3   9
   /   /
 -10  5
"""
printTree(Solution().sortedArrayToBST([-10,-3,0,5,9]))


