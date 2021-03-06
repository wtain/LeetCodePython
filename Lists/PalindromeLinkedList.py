"""
https://leetcode.com/problems/palindrome-linked-list/
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Runtime: 80 ms, faster than 50.13% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.1 MB, less than 42.22% of Python3 online submissions for Palindrome Linked List.
"""
class Solution:

    def getMiddle(self, head: ListNode) -> ListNode:
        slow: ListNode = head
        fast: ListNode = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
        return slow


    def reverse(self, head: ListNode) -> ListNode:
        prev: ListNode = None
        curr: ListNode = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        middle = self.getMiddle(head)
        middle = self.reverse(middle)
        while middle:
            if middle.val != head.val:
                return False
            middle = middle.next
            head = head.next
        return True


l1 = ListNode(1)
l1.next = ListNode(2)
print(Solution().isPalindrome(l1))  # False

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(1)
print(Solution().isPalindrome(l2))  # True
