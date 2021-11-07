"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3579/
https://leetcode.com/problems/swap-nodes-in-pairs/
"""
from Common.Leetcode import ListNode
from Common.ListUtils import print_list_nl
from Common.ObjectTestingUtils import convert_test_params_to_lists, run_functional_tests


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


tests = [
    [[1, 2, 3, 4, 5], [2, 1, 4, 3, 5]],
    [[1, 2, 3, 4], [2, 1, 4, 3]]
]

run_functional_tests(Solution().swapPairs, convert_test_params_to_lists(tests))
