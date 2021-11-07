"""
https://leetcode.com/problems/design-linked-list/

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 152 ms, faster than 86.25% of Python3 online submissions for Design Linked List.
# Memory Usage: 15.2 MB, less than 26.97% of Python3 online submissions for Design Linked List.
class MyLinkedList:

    class Node:

        def __init__(self, val, next = None):
            self.val = val
            self.next = next

    # def print(self):
    #     node = self.head
    #     while node:
    #         print(node.val, flush=True, sep=' ', end=' ')
    #         node = node.next
    #     print()

    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        result = self.head
        for i in range(index):
            result = result.next
            if not result:
                return -1

        return result.val

    def addAtHead(self, val: int) -> None:
        self.head = self.Node(val, self.head)
        if not self.last:
            self.last = self.head
        self.count += 1
        # self.print()

    def addAtTail(self, val: int) -> None:
        if not self.head:
            return self.addAtHead(val)
        self.last.next = self.Node(val)
        self.last = self.last.next
        self.count += 1
        # self.print()

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.count:
            return
        if index == self.count:
            return self.addAtTail(val)
        prev, curr = None, self.head
        for i in range(index):
            prev, curr = curr, curr.next
        if not prev:
            return self.addAtHead(val)
        prev.next = self.Node(val, curr)
        self.count += 1
        # self.print()

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return
        prev, curr = None, self.head
        for i in range(index):
            prev, curr = curr, curr.next
        if not prev:
            self.head = self.head.next
            if not self.head:
                self.last = None
            self.count -= 1
            return
        if not curr.next:
            self.last = prev
        prev.next = curr.next
        self.count -= 1
        # self.print()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


tests = [
    [
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
        [[], [1], [3], [1, 2], [1], [1], [1]],
        [null, null, null, null, 2, null, 3]
    ],
    [
        ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"],
        [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]],
        [null,null,null,null,null,null,null,null,4,null,null,null]
    ]
    # 6 1 2 4
]

run_object_tests(tests, cls=MyLinkedList, debug=False)
