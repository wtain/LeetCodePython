from typing import List

from Common.Leetcode import ListNode


def build_list(vals: List[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for v in vals:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def lists_equal(l1: ListNode, l2: ListNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 or l2:
        return False
    return True


def list_to_string(l: ListNode) -> str:
    result = ""
    while l:
        if result:
            result += ","
        result += str(l.val)
        l = l.next
    return "[" + result + "]"


def compareLists(l1: ListNode, l2: ListNode) -> bool:
    c1 = l1
    c2 = l2
    while c1 and c2:
        if c1.val != c2.val:
            return False
        c1 = c1.next
        c2 = c2.next
    return False if c1 or c2 else True