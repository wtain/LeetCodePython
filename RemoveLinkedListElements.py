"""
https://leetcode.com/problems/remove-linked-list-elements/


Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def printList(l: ListNode):
    while l:
        print(l.val, flush=True, sep=' ', end=' ')
        l = l.next
    print()


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(4)
l1.next.next.next.next.next = ListNode(5)
l1.next.next.next.next.next.next = ListNode(6)

l2 = Solution().removeElements(l1, 6)
printList(l2)  # 1->2->3->4->5

printList(Solution().removeElements(l2, 6))  # 1->2->3->4->5

printList(Solution().removeElements(None, 6))  # []

printList(Solution().removeElements(ListNode(1), 1))  # []
