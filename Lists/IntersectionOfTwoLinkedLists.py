"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Runtime: 184 ms, faster than 42.00% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 28.9 MB, less than 89.80% of Python3 online submissions for Intersection of Two Linked Lists.
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def listLength(head: ListNode) -> int:
            result = 0
            while head:
                head = head.next
                result += 1
            return result

        def advance(head: ListNode, n: int) -> ListNode:
            for i in range(n):
                head = head.next
            return head

        len1 = listLength(headA)
        len2 = listLength(headB)
        if len1 > len2:
            cnt = len1 - len2
            headA = advance(headA, cnt)
        if len2 > len1:
            cnt = len2 - len1
            headB = advance(headB, cnt)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None


l1a = ListNode(4)
l1a.next = ListNode(1)
l1a.next.next = ListNode(8)
l1a.next.next.next = ListNode(4)
l1a.next.next.next.next = ListNode(5)
l1b = ListNode(5)
l1b.next = ListNode(6)
l1b.next.next = ListNode(1)
l1b.next.next.next = l1a.next.next

print(Solution().getIntersectionNode(l1a, l1b).val)  # 8

l2a = ListNode(1)
l2a.next = ListNode(9)
l2a.next.next = ListNode(1)
l2a.next.next.next = ListNode(2)
l2a.next.next.next.next = ListNode(4)
l2b = ListNode(3)
l2b.next = l2a.next.next.next

print(Solution().getIntersectionNode(l2a, l2b).val)  # 2

l3a = ListNode(2)
l3a.next = ListNode(6)
l3a.next.next = ListNode(4)

l3b = ListNode(1)
l3b.next = ListNode(5)

print(Solution().getIntersectionNode(l3a, l3b) is None)  # True
