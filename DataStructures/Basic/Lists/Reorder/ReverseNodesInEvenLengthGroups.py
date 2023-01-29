"""
https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.



Example 1:


Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
Example 2:


Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.
Example 3:


Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 105
"""
from typing import Optional

from Common.DataTypes.Leetcode import ListNode
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists
from Common.ListUtils import build_list, print_list_range
from Common.ObjectTestingUtils import run_functional_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Runtime
# 1934 ms
# Beats
# 100%
# Memory
# 53.5 MB
# Beats
# 91.94%
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node: ListNode) -> ListNode:
            prev, current = None, node
            while current:
                next = current.next
                current.next = prev
                prev, current = current, next
            return prev

        current = head
        previous = None
        group_number = 1
        while current:
            last, next = current, current
            next = next.next
            length = 1
            for i in range(group_number-1):
                if not next:
                    break
                length += 1
                last, next = next, next.next

            if length % 2 == 0:
                last.next = None
                current_head = current
                # print_list_range(current, next)
                current = reverse(current)
                # print_list_range(current, next)
                if previous:
                    previous.next = current

                current = next
                previous = current_head
            else:
                if previous:
                    previous.next = current
                current = next
                previous = last

            group_number += 1
        return head


tests = [
    # [[1,2,3], [1,3,2]],
    # [[1,2,3,4], [1,3,2,4]],
    # [[1,2,3,4,5], [1,3,2,5,4]],
    # [[1,2,3,4,5,6], [1,3,2,6,5,4]],
    # [[1,2,3,4,5,6,7], [1,3,2,6,5,4,7]],
    [[5,2,6,3,9,1,7,3,8,4], [5,6,2,3,9,1,4,8,3,7]],
    [[1,1,0,6], [1,0,1,6]],
    [[1,1,0,6,5], [1,0,1,5,6]],
]

run_functional_tests(Solution().reverseEvenLengthGroups, convert_test_params_to_lists(tests))