"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
Accepted

"""



from typing import List

from Common.Leetcode import ListNode
from Common.ListUtils import build_list, printList
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 80 ms, faster than 5.15% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.9 MB, less than 47.02% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        w = head
        prevw = None
        r = head
        prevValue = None
        while r:
            if r.val != prevValue:
                prevValue = w.val = r.val
                prevw = w
                w = w.next
            r = r.next
        if prevw:
            prevw.next = None
        return head


tests = [
    [build_list([1,1,2]), build_list([1,2])],
    [build_list([1,1,2,3,3]), build_list([1,2,3])],
    [build_list([1,1,1]), build_list([1])],
    [build_list([1]), build_list([1])],
    [build_list([1,1]), build_list([1])],
    [build_list([]), build_list([])],
]

run_functional_tests(Solution().deleteDuplicates, tests)