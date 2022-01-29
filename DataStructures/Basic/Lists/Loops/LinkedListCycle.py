"""
https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.




Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""
from Common.DataTypes.Leetcode import ListNode

"""
Runtime: 56 ms, faster than 43.88% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.1 MB, less than 17.07% of Python3 online submissions for Linked List Cycle.

Runtime: 52 ms, faster than 44.73% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.3 MB, less than 38.17% of Python3 online submissions for Linked List Cycle.
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow: ListNode = head
        fast: ListNode = head.next
        if fast is None:
            return False

        while fast:
            if fast == slow:
                return True
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            slow = slow.next
        return False


l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = l1.next

print(Solution().hasCycle(l1))  # True

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = l2

print(Solution().hasCycle(l2))  # True


l3 = ListNode(1)

print(Solution().hasCycle(l3))  # False
