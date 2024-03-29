"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []


How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]


Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 105
"""
from Common.Constants import null
from Common.DataTypes.LeetcodeMultilevelList import Node, build_multilevel_list
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


# Runtime: 28 ms, faster than 97.49% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# Memory Usage: 15 MB, less than 46.01% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def get_last(node: Node) -> Node:
            prev = None
            while node:
                prev, node = node, node.next
            return prev

        current = head
        while current:
            tail = current.next
            if current.child:
                sublist = self.flatten(current.child)
                current.child = None

                current.next = sublist
                sublist.prev = current

                if tail:
                    last = get_last(sublist)
                    tail.prev = last
                    last.next = tail
            current = tail
        return head


# Runtime: 32 ms, faster than 91.14% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# Memory Usage: 14.7 MB, less than 72.80% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#
#         to_visit = []
#         if head:
#             to_visit.append(head)
#         prev = None
#         while to_visit:
#             # print(list(map(lambda n: n.val, to_visit)))
#             current = to_visit.pop()
#             if prev:
#                 prev.next = current
#             current.prev = prev
#             if current.next:
#                 to_visit.append(current.next)
#                 current.next = None
#             if current.child:
#                 to_visit.append(current.child)
#                 current.child = None
#             prev = current
#
#         return head


tests = [
    [
        [1,2,3,4,5,6,null,
         null,null,7,8,9,10,null,null,11,12],
        [1,2,3,7,8,11,12,9,10,4,5,6]
    ],
    [
        [1,2,null,3],
        [1,3,2]
    ],
    [
        [],
        []
    ]
]


run_functional_tests(Solution().flatten, convert_test_params(tests, build_multilevel_list))
