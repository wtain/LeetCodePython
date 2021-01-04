"""
https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
"""

"""
Runtime: 56 ms, faster than 96.37% of Python3 online submissions for Min Stacks.
Memory Usage: 18.1 MB, less than 11.35% of Python3 online submissions for Min Stacks.
"""
class MinStack:
    data = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        minv = x
        if len(self.data) > 0:
            minv = min(self.data[len(self.data)-1][1], minv)
        self.data.append([x, minv])

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[len(self.data)-1][0]

    def getMin(self) -> int:
        return self.data[len(self.data) - 1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # return -3
minStack.pop()
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2
