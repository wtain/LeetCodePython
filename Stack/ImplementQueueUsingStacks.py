"""
https://leetcode.com/problems/implement-queue-using-stacks/
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

"""
in   4 5 6
out  3 2 1

1 2 3

3 2 1
"""


"""
Runtime: 56 ms, faster than 5.15% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 14 MB, less than 7.31% of Python3 online submissions for Implement Queue using Stacks.
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ins = []
        self.outs = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.ins.append(x)

    def inToOut(self):
        while len(self.ins) > 0:
            self.outs.append(self.ins.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outs) == 0:
            self.inToOut()
        return self.outs.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.outs) == 0:
            self.inToOut()
        return self.outs[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.ins) == 0 and len(self.outs) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # 1
print(q.pop())  # 1
print(q.empty())  # False

