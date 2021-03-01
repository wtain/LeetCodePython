"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3655/
https://leetcode.com/problems/maximum-frequency-stack/

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:

Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].


Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""
import collections
import heapq


# Runtime: 340 ms, faster than 35.28% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.8 MB, less than 7.08% of Python3 online submissions for Maximum Frequency Stack.
# class FreqStack:
#
#     def __init__(self):
#         self.d = {}
#         self.h = []
#         self.ord = 0
#
#     def push(self, x: int) -> None:
#         self.d[x] = self.d.get(x, 0) + 1
#         self.ord += 1
#         heapq.heappush(self.h, (-self.d[x], -self.ord, x))
#         # print(self.h)
#
#     def pop(self) -> int:
#         f1, f2, x = heapq.heappop(self.h)
#         self.d[x] -= 1
#         return x

# Runtime: 316 ms, faster than 60.67% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.4 MB, less than 64.04% of Python3 online submissions for Maximum Frequency Stack.
class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        self.freq[x] = self.freq[x] + 1
        self.maxfreq = max(self.maxfreq, self.freq[x])
        self.group[self.freq[x]].append(x)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

def call_method(o, name, *args, **kwargs):
    # print("*** Calling " + name + " with " + str(args) + " and " + str(kwargs))
    return getattr(o, name)(*args, **kwargs)

null = None

tests = [
    (
        ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"],
        [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]],
        [null,null,null,null,null,null,null,4,null,6,null,1,null,1,null,4,2,3,9,0,4]
    ),
    (
        ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
        [[],[5],[7],[5],[7],[4],[5],[],[],[],[]],
        [null,null,null,null,null,null,null,5,7,5,4]
    )
]

for test in tests:
    methods = test[0]
    arguments = test[1]
    expected = test[2]
    n = len(methods)
    object = FreqStack()
    fail = False
    for i in range(1, n):
        output = call_method(object, methods[i], *arguments[i])
        if output != expected[i]:
            fail = True
            print("FAIL: " + str(output) + " != " + str(expected[i]))
            break
    if not fail:
        print("PASS")