"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000


Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
from typing import Optional

from Common.ObjectTestingUtils import run_functional_tests
from Common.DataTypes.Special import Node, build_special_tree_from_string
from Common.TreeUtils import build_tree_from_list

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# Runtime: 76 ms, faster than 19.16% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.7 MB, less than 31.97% of Python3 online submissions for Populating Next Right Pointers in Each Node.
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def impl(root, ends, level):
            if not root:
                return
            if len(ends) == level:
                ends.append(root)
            else:
                ends[level].next = root
                ends[level] = root
            next_level = level + 1
            impl(root.left, ends, next_level)
            impl(root.right, ends, next_level)

        impl(root, [], 0)

        return root


tests = [
    [build_tree_from_list([1,2,3,4,5,6,7]), build_special_tree_from_string("[1,#,2,3,#,4,5,6,7,#]")],
    [build_tree_from_list([]), build_special_tree_from_string("[]")],
]


run_functional_tests(Solution().connect, tests)
