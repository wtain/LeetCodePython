from collections import deque
from typing import List


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def build_multilevel_list(values: List[int]) -> Node:
    dummy = Node(0, None, None, None)
    levels = []
    parent, prev = dummy, None
    for v in values:
        if v:
            node = Node(v, prev, None, None)
            if prev:
                prev.next = node
            elif parent:
                parent.child = node
                parent = None
                levels.append(deque([]))
            levels[-1].append(node)
            prev = node
        else:
            if not levels[-1]:
                levels.pop()
            parent = levels[-1].popleft()
            prev = None
    # print(multilevel_list_to_string(dummy.child))
    return dummy.child


def is_multilevel_list(v) -> bool:
    return type(v) is Node


def list_size(v: Node) -> int:
    cnt = 0
    to_visit = [v]
    while to_visit:
        node = to_visit.pop()
        while node:
            cnt += 1
            if node.child:
                to_visit.append(node.child)
            node = node.next
    return cnt


def multilevel_list_to_string(v: Node) -> str:
    result = ""
    while v:
        result += " " + str(v.val)
        if v.child:
            result += "("
            result += multilevel_list_to_string(v.child)
            result += ")"
        v = v.next
    return result


def multilevel_list_equal(v1: Node, v2: Node) -> bool:
    if not v1 and not v2:
        return True
    if not v1 or not v2:
        return False
    to_visit1, to_visit2 = [v1], [v2]
    while to_visit1 and to_visit2:
        n1, n2 = to_visit1.pop(), to_visit2.pop()
        if n1.val != n2.val:
            return False
        if n1.next:
            to_visit1.append(n1.next)
        if n1.child:
            to_visit1.append(n1.child)
        if n2.next:
            to_visit2.append(n2.next)
        if n2.child:
            to_visit2.append(n2.child)
    if to_visit1 or to_visit2:
        return False
    return True


