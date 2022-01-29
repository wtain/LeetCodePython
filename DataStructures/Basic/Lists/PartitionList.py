"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3707/
https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from Common.Leetcode import ListNode
from Common.ListUtils import list_length, build_list
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params, convert_test_params_to_lists


# Runtime: 32 ms, faster than 80.18% of Python3 online submissions for Partition List.
# Memory Usage: 14.1 MB, less than 85.40% of Python3 online submissions for Partition List.
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        i, j, i0, j0 = None, None, None, None
        while head:
            next = head.next
            if head.val < x:
                if not i0:
                    i0 = head
                if i:
                    i.next = head
                i = head
            else:
                if not j0:
                    j0 = head
                if j:
                    j.next = head
                j = head
            head = next
        if j:
            j.next = None
        if i:
            i.next = j0
        return i0 or j0


tests = [
    [
        [1,4,3,2,5,2],
        3,
        [1,2,2,4,3,5]
    ],
    [
        [2,1],
        2,
        [1,2]
    ]
]

# print(list_length(build_list(tests[0][0])))
# print(list_length(build_list(tests[1][0])))

run_functional_tests(Solution().partition, convert_test_params_to_lists(tests, [0, 2]))
