"""
https://leetcode.com/problems/all-oone-data-structure/

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(Strings key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(Strings key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".


Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"


Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
"""

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# WRONG - same values
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
#
#
# class DoubleLinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def insert(self, value) -> Node:
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         return new_node
#
#     def remove(self, node: Node):
#         if node.prev:
#             node.prev.next = node.next
#         else:
#             self.head = node.next
#         if node.next:
#             node.next.prev = node.prev
#         else:
#             self.tail = node.prev
#
#     def swap_with_next(self, node1: Node):
#         node2 = node1.next
#         node0 = node1.prev
#         node3 = node2.next
#
#         node1.next = node3
#         if node3:
#             node3.prev = node1
#         else:
#             self.tail = node1
#
#         node2.next = node1
#         node1.prev = node2
#
#         if node0:
#             node0.next = node2
#         else:
#             self.head = node2
#         node2.prev = node0
#
#     def print(self):
#         node = self.head
#         while node:
#             print(node.val, flush=True, sep=' ', end=' ')
#             node = node.next
#         print()
#
#
# class AllOne:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.list = DoubleLinkedList()
#         self.hash = dict()
#
#     def print(self):
#         self.list.print()
#
#     def inc(self, key: str) -> None:
#         """
#         Inserts a new key <Key> with value 1. Or increments an existing key by 1.
#         """
#         print("INC", key)
#         if key not in self.hash:
#             node = self.list.insert([key, 1])
#             self.hash[key] = node
#         else:
#             node = self.hash.get(key)
#             node.val[1] += 1
#             if node.next and node.next.val[1] < node.val[1]:
#                 self.list.swap_with_next(node)
#         self.print()
#
#     def dec(self, key: str) -> None:
#         """
#         Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
#         """
#         print("DEC", key)
#         node = self.hash.get(key)
#         node.val[1] -= 1
#         if node.val[1] == 0:
#             self.list.remove(node)
#             del self.hash[key]
#         elif node.prev and node.prev.val[1] > node.val[1]:
#             DoubleLinkedList.swap_with_next(node.prev)
#         self.print()
#
#     def getMaxKey(self) -> str:
#         """
#         Returns one of the keys with maximal value.
#         """
#         return self.list.tail.val[0] if self.list.tail else ""
#
#     def getMinKey(self) -> str:
#         """
#         Returns one of the keys with Minimal value.
#         """
#         return self.list.head.val[0] if self.list.head else ""


# WRONG, UNFINISHED
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
#
#
# class DoubleLinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def insert(self, value) -> Node:
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         return new_node
#
#     def remove(self, node: Node):
#         if node.prev:
#             node.prev.next = node.next
#         else:
#             self.head = node.next
#         if node.next:
#             node.next.prev = node.prev
#         else:
#             self.tail = node.prev
#
#     def swap_with_next(self, node1: Node):
#         node2 = node1.next
#         node0 = node1.prev
#         node3 = node2.next
#
#         node1.next = node3
#         if node3:
#             node3.prev = node1
#         else:
#             self.tail = node1
#
#         node2.next = node1
#         node1.prev = node2
#
#         if node0:
#             node0.next = node2
#         else:
#             self.head = node2
#         node2.prev = node0
#
#     def print(self):
#         node = self.head
#         while node:
#             print(node.val, flush=True, sep=' ', end=' ')
#             node = node.next
#         print()
#
#     def is_empty(self) -> bool:
#         return self.head is None
#
#
#
# class AllOne:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.list = DoubleLinkedList()
#         self.key_to_node = dict()
#         self.count_to_node = dict()
#
#     def print(self):
#         self.list.print()
#
#     def get_or_insert_count_node(self, cnt: int):
#         if cnt not in self.count_to_node:
#             self.count_to_node = self.list.insert([DoubleLinkedList(), cnt])
#         return self.count_to_node.get(cnt)
#
#     def inc(self, key: str) -> None:
#         """
#         Inserts a new key <Key> with value 1. Or increments an existing key by 1.
#         """
#         # print("INC", key)
#         if key not in self.key_to_node:
#             node = self.get_or_insert_count_node(1)
#             inner_node = node.val[0].insert([key, node])
#             self.key_to_node[key] = inner_node
#         else:
#             inner_node = self.key_to_node[key]
#             keys, count = inner_node.parent.val
#             keys.remove(inner_node)
#
#             node = self.get_or_insert_count_node(count+1)
#             inner_node.value[1] = node
#
#             if keys.is_empty():
#                 del self.count_to_node[count]
#         # self.print()
#
#     def dec(self, key: str) -> None:
#         """
#         Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
#         """
#         # print("DEC", key)
#         node = self.hash.get(key)
#         node.val[1] -= 1
#         if node.val[1] == 0:
#             self.list.remove(node)
#             del self.hash[key]
#         elif node.prev and node.prev.val[1] > node.val[1]:
#             DoubleLinkedList.swap_with_next(node.prev)
#         # self.print()
#
#     def getMaxKey(self) -> str:
#         """
#         Returns one of the keys with maximal value.
#         """
#         return self.list.tail.val[0] if self.list.tail else ""
#
#     def getMinKey(self) -> str:
#         """
#         Returns one of the keys with Minimal value.
#         """
#         return self.list.head.val[0] if self.list.head else ""


# Runtime: 3972 ms, faster than 6.11% of Python3 online submissions for All O`one Data Structure.
# Memory Usage: 29.9 MB, less than 37.99% of Python3 online submissions for All O`one Data Structure.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_to_front(self, value) -> Node:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return new_node

    def insert_after(self, node: Node, value) -> Node:
        new_node = Node(value)
        new_node.next = node.next
        new_node.prev = node
        if new_node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node
        return new_node

    def remove(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def swap_with_next(self, node1: Node):
        node2 = node1.next
        node0 = node1.prev
        node3 = node2.next

        node1.next = node3
        if node3:
            node3.prev = node1
        else:
            self.tail = node1

        node2.next = node1
        node1.prev = node2

        if node0:
            node0.next = node2
        else:
            self.head = node2
        node2.prev = node0

    def print(self):
        node = self.head
        while node:
            print(node.val, flush=True, sep=' ', end=' ')
            node = node.next
        print()

    def is_empty(self) -> bool:
        return self.head is None


class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = DoubleLinkedList()
        self.key_to_count = dict()
        self.count_to_node = dict()

    def print(self):
        self.list.print()

    def update_count_for_key(self, key: str, old_count: int, new_count: int):
        old_count_node = self.count_to_node[old_count]
        old_count_node.val[1].remove(key)
        if new_count:
            if new_count not in self.count_to_node:
                new_count_node = self.list.insert_after(old_count_node, [new_count, set()])
                self.count_to_node[new_count] = new_count_node
            self.count_to_node[new_count].val[1].add(key)
        if not old_count_node.val[1]:
            self.list.remove(old_count_node)
            del self.count_to_node[old_count]


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # print("INC", key)
        if key in self.key_to_count:
            old_count = self.key_to_count[key]
            new_count = old_count + 1
            self.key_to_count[key] += 1
            self.update_count_for_key(key, old_count, new_count)
        else:
            self.key_to_count[key] = 1
            if 1 not in self.count_to_node:
                node1 = self.list.insert_to_front([1, set()])
                self.count_to_node[1] = node1
            self.count_to_node[1].val[1].add(key)
        # self.print()

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        # print("DEC", key)
        old_count = self.key_to_count[key]
        new_count = old_count - 1
        self.key_to_count[key] -= 1
        if not self.key_to_count[key]:
            del self.key_to_count[key]
        self.update_count_for_key(key, old_count, new_count)
        # self.print()

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return list(self.list.tail.val[1])[0] if self.list.tail else ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return list(self.list.head.val[1])[0] if self.list.head else ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


tests = [
    [
        ["AllOne","inc","inc","inc","inc","inc","inc","getMaxKey","inc","dec","getMaxKey","dec","inc","getMaxKey","inc","inc","dec","dec","dec","dec","getMaxKey","inc","inc","inc","inc","inc","inc","getMaxKey","getMinKey"],
        [[],["hello"],["world"],["leet"],["code"],["ds"],["leet"],[],["ds"],["leet"],[],["ds"],["hello"],[],["hello"],["hello"],["world"],["leet"],["code"],["ds"],[],["new"],["new"],["new"],["new"],["new"],["new"],[],[]],
        [null,null,null,null,null,null,null,"leet",null,null,"ds",null,null,"hello",null,null,null,null,null,null,"hello",null,null,null,null,null,null,"new","hello"]
    ],
    [
        ["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"],
        [[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]],
        [null,null,null,null,null,"hello",null,null,null,null,null,null,null,"leet"]
    ],
    [
        ["AllOne","getMaxKey","getMinKey"],
        [[],[],[]],
        [null, "", ""]
    ],
    [
        ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"],
        [[], ["hello"], ["hello"], [], [], ["leet"], [], []],
        [null, null, null, "hello", "hello", null, "hello", "leet"]
    ]
]

run_object_tests(tests, cls=AllOne)