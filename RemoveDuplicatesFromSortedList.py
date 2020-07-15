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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


printList(Solution().deleteDuplicates(createList([1,1,2])))  # 1 2
printList(Solution().deleteDuplicates(createList([1,1,2,3,3])))  # 1 2 3
printList(Solution().deleteDuplicates(createList([1,1,1])))  # 1
printList(Solution().deleteDuplicates(createList([1])))  # 1
printList(Solution().deleteDuplicates(createList([1,1])))  # 1
printList(Solution().deleteDuplicates(createList([])))  #

