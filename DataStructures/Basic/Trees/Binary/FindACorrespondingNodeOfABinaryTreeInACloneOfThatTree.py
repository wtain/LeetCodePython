"""
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.



Example 1:


Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:


Input: tree = [7], target =  7
Output: 7
Example 3:


Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
Example 4:


Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5
Example 5:


Input: tree = [1,2,null,3], target = 2
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.


Runtime: 608 ms, faster than 88.54% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
Memory Usage: 24 MB, less than 66.17% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
"""
from Common.DataTypes.Leetcode import TreeNode
from Common.TreeUtils import cloneTree


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original is target:
            return cloned
        resultLeft = self.getTargetCopy(original.left, cloned.left, target)
        if resultLeft:
            return resultLeft
        return self.getTargetCopy(original.right, cloned.right, target)



root1 = TreeNode(7)
root1.left = TreeNode(4)
root1.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(19)

print(Solution().getTargetCopy(root1, cloneTree(root1), root1.right).val)  # 3


root2 = TreeNode(7)

print(Solution().getTargetCopy(root2, cloneTree(root2), root2).val)  # 7


root3 = TreeNode(8)
root3.right = TreeNode(6)
root3.right.right = TreeNode(5)
root3.right.right.right = TreeNode(4)
root3.right.right.right.right = TreeNode(3)
root3.right.right.right.right.right = TreeNode(2)
root3.right.right.right.right.right.right = TreeNode(1)

print(Solution().getTargetCopy(root3, cloneTree(root3), root3.right.right.right).val)  # 4


