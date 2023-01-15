from typing import List

from Common.DataTypes.Leetcode import ListNode


def build_list(vals: List[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for v in vals:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def get_list_node(node: ListNode, pos: int) -> ListNode:
    while pos and node:
        node = node.next
        pos -= 1
    return node


def build_list_with_loop(vals: List[int], pos: int) -> ListNode:
    l = build_list(vals)
    if pos == -1:
        return l
    node, last = get_list_node(l, pos), get_list_node(l, len(vals)-1)
    last.next = node
    return l


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
    visited = set()
    while l:
        if result:
            result += ","
        result += str(l.val)
        visited.add(id(l))
        l = l.next
        if id(l) in visited:
            result += "... (loop)"
            break
    return "[" + result + "]"


def list_length(l: ListNode) -> int:
    result = 0
    while l:
        result += 1
        l = l.next
    return result


def list_length_loop_proof(head: ListNode) -> int:
    slow, fast = head, head
    if not slow:
        return 0
    slow, fast = slow.next, fast.next
    if not fast:
        return 1
    result = 1
    fast = fast.next
    while fast and id(slow) != id(fast):
        result += 1
        slow, fast = slow.next, fast.next
        if not fast:
            return result+1
        fast = fast.next
    if id(slow) != id(fast):
        return result
    fast = head
    steps = 1
    while id(slow) != id(fast):
        slow, fast = slow.next, fast.next
        steps += 1
    return result + steps // 2


def compareLists(l1: ListNode, l2: ListNode) -> bool:
    c1 = l1
    c2 = l2
    while c1 and c2:
        if c1.val != c2.val:
            return False
        c1 = c1.next
        c2 = c2.next
    return False if c1 or c2 else True


def buildNumberAsList(arr: List[int]) -> ListNode:
    h = build_list(arr)

    if not h:
        return ListNode(0)
    return h


def printList(l: ListNode, new_line=False):
    while l:
        print(l.val, flush=True, sep=' ', end=' ')
        l = l.next
    if new_line:
        print()


def print_list_nl(l: ListNode):
    printList(l, True)


def print_list_n(nums: List[int], cnt: int):
    for i in range(cnt):
        print(nums[i], flush=True, sep=' ', end=' ')
    print()


def list_copy_n(nums: List[int], cnt: int):
    return nums[:cnt]


def print_list_range(current: ListNode, afterEnd: ListNode):
    while current and current != afterEnd:
        print(current.val, flush=True, sep=' ', end=' ')
        current = current.next
    print()