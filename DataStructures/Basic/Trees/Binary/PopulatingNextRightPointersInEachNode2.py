"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100


Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
from Common.Constants import null
from Common.ObjectTestingUtils import run_functional_tests
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
from Common.DataTypes.NextTree import Node, build_next_tree_from_list


# Runtime: 53 ms, faster than 78.31% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 15.3 MB, less than 92.97% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def impl(node: Node, vnext, level):
            if level == len(vnext):
                vnext.append(node)
            else:
                vnext[level].next = node
                vnext[level] = node
            if node.left:
                impl(node.left, vnext, level+1)
            if node.right:
                impl(node.right, vnext, level + 1)

        impl(root, [], 0)
        return root


tests = [
    [
        build_tree_from_list([1,2,3,4,5,null,7]),
        build_next_tree_from_list([1,'#',2,3,'#',4,5,7,'#'])
    ],
    [
        None,
        None
    ]
]

run_functional_tests(Solution().connect, tests)
