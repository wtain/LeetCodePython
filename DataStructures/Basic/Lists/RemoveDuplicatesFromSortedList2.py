"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

Runtime: 44 ms, faster than 41.95% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 14.3 MB, less than 22.81% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
from Common.Leetcode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        newHead = ListNode()
        newCurrent = newHead
        while current:
            next = current.next
            current0 = current
            while next and next.val == current.val:
                current = next
                next = next.next
            if current == current0:
                newCurrent.next = current
                newCurrent = newCurrent.next
                newCurrent.next = None
            current = next
        return newHead.next


def printList(l: ListNode):
    while l:
        print(l.val, flush=True, sep=' ', end=' ')
        l = l.next
    print()


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(4)
l1.next.next.next.next.next = ListNode(4)
l1.next.next.next.next.next.next = ListNode(5)

printList(Solution().deleteDuplicates(l1))  # 1 2 5

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(1)
l2.next.next.next = ListNode(2)
l2.next.next.next.next = ListNode(3)

printList(Solution().deleteDuplicates(l2))  # 2 3