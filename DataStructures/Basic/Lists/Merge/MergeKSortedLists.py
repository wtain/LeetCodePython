"""
https://leetcode.com/problems/merge-k-sorted-lists/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""


import heapq
from typing import List

from Common.DataTypes.Leetcode import ListNode


# Runtime: 128 ms, faster than 36.99% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18.6 MB, less than 15.14% of Python3 online submissions for Merge k Sorted Lists.
from Common.ListUtils import build_list, compareLists, printList


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class ListEntry:
            def __init__(self, h: ListNode):
                self.h = h

            def __lt__(self, other):
                return self.h.val < other.h.val

        lists_heap = [ListEntry(le) for le in lists if le]
        heapq.heapify(lists_heap)
        head = ListNode()
        prev = head
        while lists_heap:
            list_entry = heapq.heappop(lists_heap)
            ln = list_entry.h.next
            prev.next = list_entry.h
            prev = prev.next
            if ln:
                list_entry.h = ln
                heapq.heappush(lists_heap, list_entry)
        return head.next


tests = [
    (
        [[]],
        []
    ),

    (
        [],
        []
    ),

    (
        [build_list([1,4,5]),
        build_list([1,3,4]),
        build_list([2,6])],
        build_list([1,1,2,3,4,4,5,6])
    )
]

for test in tests:
    result = Solution().mergeKLists(test[0])
    if compareLists(result, test[1]):
        print("PASS")
    else:
        print("FAIL - [", flush=True, sep=' ', end=' ')
        printList(result)
        print("]")