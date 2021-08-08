"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3871/
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]


Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
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


# Runtime: 52 ms, faster than 68.27% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 15.9 MB, less than 97.69% of Python3 online submissions for N-ary Tree Level Order Traversal.
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        toVisit = []
        result = []
        if root:
            toVisit.append(root)
        while toVisit:
            level = []
            next_level = []
            for node in toVisit:
                level.append(node.val)
                if node.children:
                    for child in node.children:
                        next_level.append(child)
            result.append(level)
            toVisit = next_level
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
        [[1],[3,2,4],[5,6]]
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
        [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
    ]
]


run_functional_tests(Solution().levelOrder, tests)