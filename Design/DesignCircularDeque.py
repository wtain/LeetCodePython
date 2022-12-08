"""
https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.


Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4


Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
"""
from Common.Constants import true, false, null
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# 87 ms
# Beats
# 79.47%
# Memory
# 15 MB
# Beats
# 14.2%
class MyCircularDeque:

    class Node:

        def __init__(self, value: int):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, k: int):
        self.max_size = k
        self.current_size = 0
        self.start = None
        self.end = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = MyCircularDeque.Node(value)
        if self.isEmpty():
            self.start = new_node
            self.end = new_node
        else:
            self.start.prev = new_node
            new_node.next = self.start
            self.start = new_node
        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = MyCircularDeque.Node(value)
        if self.isEmpty():
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.current_size -= 1
        self.start = self.start.next
        if self.current_size:
            self.start.prev = None
        else:
            self.end = None
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.current_size -= 1
        self.end = self.end.prev
        if self.current_size:
            self.end.next = None
        else:
            self.start = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.start.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.end.value

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.max_size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


tests = [
    [
        ["MyCircularDeque","insertFront","deleteLast","getRear","getFront","getFront","deleteFront","insertFront","insertLast","insertFront","getFront","insertFront"],
        [[4],[9],[],[],[],[],[],[6],[5],[9],[],[6]],
        [null,true,true,-1,-1,-1,false,true,true,true,9,true]
    ],
    [
        ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"],
        [[3], [1], [2], [3], [4], [], [], [], [4], []],
        [null, true, true, true, false, 2, true, true, true, 4]
    ]
]

run_object_tests(tests, cls=MyCircularDeque)
