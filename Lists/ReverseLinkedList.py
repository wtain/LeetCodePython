"""
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Runtime: 52 ms, faster than 24.51% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.3 MB, less than 62.20% of Python3 online submissions for Reverse Linked List.
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev: ListNode = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


def printList(l: ListNode):
    while l:
        print(l.val, flush=True, sep=' ', end=' ')
        l = l.next
    print()


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

printList(Solution().reverseList(l))  # 5 4 3 2 1

