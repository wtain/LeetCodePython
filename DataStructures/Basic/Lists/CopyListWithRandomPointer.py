"""
https://leetcode.com/problems/copy-list-with-random-pointer/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.


Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.

Runtime: 52 ms, faster than 5.82% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.7 MB, less than 87.65% of Python3 online submissions for Copy List with Random Pointer.
"""



from typing import List




# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         curr = head
#         cache: Dict[Node, Node] = {}
#         while curr:
#             newNode = Node(curr.val)
#             cache[curr] = newNode
#             curr = curr.next
#         curr = head
#         while curr:
#             cache[curr].next = cache.get(curr.next, None)
#             cache[curr].random = cache.get(curr.random, None)
#             curr = curr.next
#         return cache.get(head, None)


# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         curr = head
#         newHead = None
#         newPrev = None
#         while curr:
#             next = curr.next
#             newCurr = Node(curr.val)
#             newCurr.random = curr.random
#             if not newHead:
#                 newHead = newCurr
#             if newPrev:
#                 newPrev.next = newCurr
#             newPrev = newCurr
#             curr.next = newCurr
#             curr = next
#
#         newCurr = newHead
#         curr = head
#         while newCurr:
#             if curr.random:
#                 curr.random = curr.random.next # new random
#             newCurr.random = curr.random.next
#             newCurr = newCurr.next
#
#         newCurr = newHead
#         curr = head
#         while newCurr:
#             next = newCurr.next.random if newCurr.next else None
#             newRandom = curr.random
#
#             newCurr.random = newRandom
#             curr.random = newRandom.random
#             curr.next = next
#
#             curr = curr.next
#             newCurr = newCurr.next
#         return newHead

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         curr = head
#         newHead = None
#         while curr:
#             newCurr = Node(curr.val)
#             newCurr.random = curr.random
#             # newCurr.next = curr
#             curr.random = newCurr
#             if not newHead:
#                 newHead = newCurr
#             curr = curr.next
#         curr = head
#         while curr:
#             newCurr = curr.random
#             if curr.next:
#                 newCurr.next = curr.next.random
#             curr = curr.next
#         curr = head
#         newCurr = newHead
#         while curr:
#             random = newCurr.random
#             if newCurr.random:
#                 newCurr.random = newCurr.random.random
#             curr.random = random
#             curr = curr.next
#             newCurr = newCurr.next
#         return newHead

# Runtime: 40 ms, faster than 26.60% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.8 MB, less than 88.50% of Python3 online submissions for Copy List with Random Pointer.
from Common.DataTypes.Leetcode import Node


# Runtime: 57 ms, faster than 40.29% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15 MB, less than 29.48% of Python3 online submissions for Copy List with Random Pointer.
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            curr2 = Node(curr.val)
            curr2.next = curr.next
            curr.next = curr2
            curr = curr2.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        head2 = head.next if head else None
        while curr:
            curr2 = curr.next
            next = curr2.next
            curr.next = next
            curr2.next = next.next if next else None
            curr = next
        return head2


def buildList(l: List[List[int]]) -> Node:
    nodes: List[Node] = []
    for i, n in enumerate(l):
        node = Node(n[0])
        nodes.append(node)
    for i, n in enumerate(l):
        if n[1] is not None:
            nodes[i].random = nodes[n[1]]
        if i+1 < len(nodes):
            nodes[i].next = nodes[i+1]
    return nodes[0] if nodes else None


def listsEqual(h1: Node, h2: Node) -> bool:
    toVisit = [(h1, h2)]
    visited = []
    while toVisit:
        n1, n2 = toVisit.pop()
        if not n1 and not n2:
            break
        if not n1 or not n2:
            return False
        if n1 == n2 or n1.val != n2.val:
            return False
        visited.append(n1.val)
        if n1.next and n2.next:
            if n1.next.val not in visited:
                toVisit.append((n1.next, n2.next))
        elif n1.next or n2.next:
            return False
        if n1.random and n2.random:
            if n1.random.val not in visited:
                toVisit.append((n1.random, n2.random))
        elif n1.random or n2.random:
            return False
    return True


def renderList(head: Node) -> List[List[int]]:
    result = []
    curr = head
    i = 0
    d = {}
    while curr:
        d[curr] = i
        curr = curr.next
        i += 1
    curr = head
    while curr:
        val = curr.val
        random_idx = None
        if curr.random:
            random_idx = d[curr.random]
        result.append([val, random_idx])
        curr = curr.next
    return result


null = None

tests = [
    [[7,null],[13,0],[11,4],[10,2],[1,0]],
    [[1,1],[2,1]],
    [[3,null],[3,0],[3,null]],
    []
]

for test in tests:
    list = buildList(test)
    result = Solution().copyRandomList(list)
    if listsEqual(list, result):
        print("PASS")
    else:
        print("FAIL - " + str(renderList(result)))