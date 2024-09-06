"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2024-09-06

You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.



Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:



Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:



No node has value 5.



Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
All elements in nums are unique.
The number of nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
The input is generated such that there is at least one node in the linked list that has a value not present in nums.
"""
from typing import Optional, List

from Common.DataTypes.Leetcode import ListNode
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime
# 696
# ms
# Beats
# 94.01%
# Analyze Complexity
# Memory
# 55.88
# MB
# Beats
# 52.33%
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hash = set(nums)
        lead = ListNode(0, head)
        prev, curr = lead, head
        while curr:
            if curr.val in hash:
                prev.next = curr.next
                curr = curr.next
            else:
                nx = curr.next
                prev = curr
                curr = nx

        return lead.next


tests = [
    [[1,2,3], [1,2,3,4,5], [4,5]],
    [[1], [1,2,1,2,1,2], [2,2,2]],
    [[5], [1,2,3,4], [1,2,3,4]],
]

run_functional_tests(Solution().modifiedList, convert_test_params_to_lists(tests, indexes=[1,2]))
