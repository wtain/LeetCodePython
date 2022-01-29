"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/640/week-5-september-29th-september-30th/3992/
https://leetcode.com/problems/split-linked-list-in-parts/

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.



Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List

from Common.Leetcode import ListNode
from Common.ListUtils import compareLists, build_list
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.TestParamsHelpers import convert_test_params_to_lists


# Runtime: 40 ms, faster than 65.79% of Python3 online submissions for Split Linked List in Parts.
# Memory Usage: 14.7 MB, less than 89.47% of Python3 online submissions for Split Linked List in Parts.
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        def get_len(head: ListNode) -> int:
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt

        n = get_len(head)
        li, mod = n // k, n % k
        if mod:
            li += 1

        result = [None for _ in range(k)]

        cli, clen = 0, 0
        while head:
            nx = head.next
            if not clen:
                result[cli] = head
            clen += 1
            if clen == li:
                clen = 0
                if mod and cli + 1 == mod:
                    li -= 1
                head.next = None
                cli += 1
            head = nx
        return result


tests = [
    [[1,2,3], 5, [[1],[2],[3],[],[]]],
    [[1,2,3,4,5,6,7,8,9,10], 3, [[1,2,3,4],[5,6,7],[8,9,10]]]
]


def customCheck(test, result) -> bool:
    if len(test[-1]) != len(result):
        return False
    for le, lr in zip(test[-1], result):
        if not compareLists(build_list(le), lr):
            return False
    return True


run_functional_tests(Solution().splitListToParts, convert_test_params_to_lists(tests, [0]), custom_check=customCheck)
