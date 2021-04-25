"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3714/
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

from Common.NAryTree import Node
from Common.ObjectTestingUtils import run_functional_tests

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Runtime: 48 ms, faster than 80.92% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.1 MB, less than 63.08% of Python3 online submissions for N-ary Tree Preorder Traversal.
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            result.append(node.val)
            if node.children:
                for child in node.children[::-1]:
                    st.append(child)
        return result


tests = [
    [
        Node(1, [
            Node(3, [
                Node(5),
                Node(6)
            ]),
            Node(2),
            Node(4)
        ]),
        [1,3,5,6,2,4]
    ],
    [
        Node(1, [
            Node(2),
            Node(3, [
                Node(6),
                Node(7, [
                    Node(11, [
                        Node(14)
                    ])
                ])
            ]),
            Node(4, [
                Node(8, [
                    Node(12)
                ])
            ]),
            Node(5, [
                Node(9, [
                    Node(13)
                ]),
                Node(10)
            ])
        ]),
        [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
    ]
]

run_functional_tests(Solution().preorder, tests)