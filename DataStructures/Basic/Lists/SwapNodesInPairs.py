"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3579/
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        newHead = head.next
        prev = None
        current = head
        while current and current.next:
            next = current.next
            tail = next.next

            current.next = tail
            next.next = current

            if prev:
                prev.next = next

            prev = current
            current = tail
        return newHead


def printList(l: ListNode):
    while l:
        print(l.val, flush=True, sep=' ', end=' ')
        l = l.next
    print()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
printList(Solution().swapPairs(list1))

list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(3)
list2.next.next.next = ListNode(4)
printList(Solution().swapPairs(list2))