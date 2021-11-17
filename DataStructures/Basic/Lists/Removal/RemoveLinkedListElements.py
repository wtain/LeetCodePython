"""
https://leetcode.com/problems/remove-linked-list-elements/


Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
from Common.Leetcode import ListNode
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 60 ms, faster than 98.67% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 16.9 MB, less than 65.64% of Python3 online submissions for Remove Linked List Elements.
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        read = head
        write = head
        prev = None
        while read:
            if read.val != val:
                write.val = read.val
                prev = write
                write = write.next
            read = read.next
        if prev:
            prev.next = None
        else:
            return None
        return head


tests = [
    [build_list([1, 2, 6, 3, 4, 5, 6]), 6, build_list([1, 2, 3, 4, 5])],
    [build_list([1, 2, 3, 4, 5]), 6, build_list([1, 2, 3, 4, 5])],
    [None, 6, None],
    [build_list([1]), 1, None]
]

run_functional_tests(Solution().removeElements, tests)
