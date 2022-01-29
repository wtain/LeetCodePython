"""
https://leetcode.com/problems/linked-list-random-node/
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.



Example 1:

Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.


Constraints:

The number of nodes in the linked list will be in the range [1, 104]
-104 <= Node.val <= 104
At most 104 calls will be made to getRandom.


Follow up:

What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?
"""


# Definition for singly-linked list.
from random import random

# WRONG
# class Solution:
#
#     def __init__(self, head: ListNode):
#         """
#         @param head The linked list's head.
#         Note that the head is guaranteed to be not null, so it contains at least one node.
#         """
#         self.head = head
#
#     def getRandom(self) -> int:
#         """
#         Returns a random node's value.
#         """
#         k = 3
#         current = self.head
#
#         S = [0] * k
#
#         for i in range(k):
#             S[i] = current.val
#             current = current.next
#             if not current:
#                 return S[randint(0, i)]
#
#         result = current.val
#         W = exp(log(random()) / k)
#         while current:
#             n = int(log(random())/log(1-W)) + 1
#             for _ in range(n):
#                 current = current.next
#                 if not current:
#                     break
#                 S[randint(0, k-1)] = current.val
#                 W *= exp(log(random()) / k)
#
#         return S[randint(0, k-1)]

# Runtime: 88 ms, faster than 54.69% of Python3 online submissions for Linked List Random Node.
# Memory Usage: 17.2 MB, less than 89.26% of Python3 online submissions for Linked List Random Node.
from Common.DataTypes.Leetcode import ListNode
from Common.ListUtils import build_list


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        current = self.head

        result = current.val
        cnt = 1
        while current:
            if random() < 1 / cnt:
                result = current.val
            cnt += 1
            current = current.next

        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()




n_samples = 1000
n_values = 10
head = build_list(range(n_values))
s = Solution(head)
hist = [0] * n_values
for i in range(n_samples):
    j = s.getRandom()
    hist[j] += 1

for i in range(n_values):
    print(i, hist[i] / n_samples)