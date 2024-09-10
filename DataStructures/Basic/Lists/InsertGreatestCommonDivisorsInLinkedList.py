"""
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.



Example 1:


Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
Example 2:


Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.


Constraints:

The number of nodes in the list is in the range [1, 5000].
1 <= Node.val <= 1000
"""
import math
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists
from Common.ObjectTestingUtils import run_functional_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime
# 76
# ms
# Beats
# 36.51%
# Analyze Complexity
# Memory
# 19.62
# MB
# Beats
# 36.27%
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            if prev:
                prev.next = ListNode(math.gcd(prev.val, curr.val), curr)
            nx = curr.next
            prev = curr
            curr = nx
        return head


tests = [
    [[18,6,10,3], [18,6,6,2,10,1,3]],
    [[7], [7]],
]

run_functional_tests(Solution().insertGreatestCommonDivisors, convert_test_params_to_lists(tests))
