"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:





Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""
from Common.DataTypes.Leetcode import ListNode

"""
Runtime: 44 ms, faster than 33.28% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.4 MB, less than 5.36% of Python3 online submissions for Delete Node in a Linked List.
"""
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev2 = None
        prev = None
        curr = node
        while curr:
            if curr.next:
                curr.val = curr.next.val
            prev2 = prev
            prev = curr
            curr = curr.next
        if prev2:
            prev2.next = None


def printList(l: ListNode):
    while l:
        print(l.val, flush=True, sep=' ', end=' ')
        l = l.next
    print()


l1 = ListNode(4)
n5 = l1.next = ListNode(5)
l1.next.next = ListNode(1)
l1.next.next.next = ListNode(9)

Solution().deleteNode(n5)

printList(l1)  # 4 1 9

l2 = ListNode(4)
l2.next = ListNode(5)
n1 = l2.next.next = ListNode(1)
l2.next.next.next = ListNode(9)

Solution().deleteNode(n1)

printList(l2)  # 4 5 9
