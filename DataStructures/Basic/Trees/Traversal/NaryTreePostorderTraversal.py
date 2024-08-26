"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-26

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)



Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

from Common.DataTypes.NAryTree import Node
from Common.ObjectTestingUtils import run_functional_tests

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Runtime
# 47
# ms
# Beats
# 45.79%
# Analyze Complexity
# Memory
# 18.08
# MB
# Beats
# 95.62%
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        nodes = []
        if root:
            nodes.append([root, 0])
        while nodes:
            ni = nodes[-1]
            if not ni[0].children or ni[1] == len(ni[0].children):
                nodes.pop()
                result.append(ni[0].val)
            else:
                nodes.append([ni[0].children[ni[1]], 0])
                ni[1] += 1
        return result


tests = [
    [
        # [1,null,3,2,4,null,5,6]
        Node(1, [
             Node(3, [
                 Node(5),
                 Node(6)
             ]),
             Node(2),
             Node(4)
            ])
        ,
        [5,6,3,2,4,1]
    ],
    [
        # [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
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
        ])
        ,
        [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
    ],
]

run_functional_tests(Solution().postorder, tests)
