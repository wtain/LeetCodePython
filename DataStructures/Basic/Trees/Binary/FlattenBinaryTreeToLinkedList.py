"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3742/
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.FunctionalHelpers import make_inplace


# Runtime: 32 ms, faster than 91.72% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 73.24% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Solution:

    def flatten(self, root: TreeNode) -> None:

        def impl(root: TreeNode) -> TreeNode:
            if not root:
                return None
            left_end = impl(root.left)
            right_end = impl(root.right)
            right = root.right
            root.right = root.left
            root.left = None
            if left_end:
                left_end.right = right
            else:
                root.right = right

            if right_end:
                return right_end
            if left_end:
                return left_end

            return root

        return impl(root)


tests = [
    [
        TreeNode(1,
                 TreeNode(2,
                          TreeNode(3),
                          TreeNode(4)),
                 TreeNode(5,
                          null,
                          TreeNode(6))),
        TreeNode(1, null,
                 TreeNode(2, null,
                          TreeNode(3, null,
                                   TreeNode(4, null,
                                            TreeNode(5, null,
                                                     TreeNode(6))))))
    ],
    [
        null,
        null
    ],
    [
        TreeNode(0),
        TreeNode(0)
    ]
]

run_functional_tests(make_inplace(Solution().flatten), tests)