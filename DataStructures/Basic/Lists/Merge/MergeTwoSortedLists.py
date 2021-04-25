"""
https://leetcode.com/problems/merge-two-sorted-lists/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3592/
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Runtime: 32 ms, faster than 91.61% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.2 MB, less than 49.62% of Python3 online submissions for Merge Two Sorted Lists.
"""
from typing import List

from Common.Leetcode import ListNode

"""
Runtime: 48 ms, faster than 26.85% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.6 MB, less than 95.56% of Python3 online submissions for Merge Two Sorted Lists.
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head: ListNode = None
        prev: ListNode = None
        while l1 and l2:
            n: ListNode = None
            if l1.val < l2.val:
                n = l1
                l1 = l1.next
            else:
                n = l2
                l2 = l2.next
            if prev:
                prev.next = n
            prev = n
            if not head:
                head = n
        while l1:
            if prev:
                prev.next = l1
            prev = l1
            if not head:
                head = l1
            l1 = l1.next
        while l2:
            if prev:
                prev.next = l2
            prev = l2
            if not head:
                head = l2
            l2 = l2.next
        if prev:
            prev.next = None
        return head


def printList(l: ListNode):
    while l:
        print(l.val, flush=True, sep=' ', end=' ')
        l = l.next
    print()


def createList(a: List[int]) -> ListNode:
    head = None
    prev: ListNode = None
    for i in a:
        n = ListNode(i)
        if prev:
            prev.next = n
        else:
            head = n
        prev = n
    return head


printList(Solution().mergeTwoLists(createList([1, 2, 4]), createList([1, 3, 4])))  # 1 1 2 3 4 4

printList(Solution().mergeTwoLists(createList([1, 2, 4]), createList([])))  # 1 2 4
printList(Solution().mergeTwoLists(createList([]), createList([1, 3, 4])))  # 1 3 4

printList(Solution().mergeTwoLists(createList([]), createList([])))  #