"""
https://leetcode.com/problems/rle-iterator/

We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.

For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are also valid RLE of arr.
Given a run-length encoded array, design an iterator that iterates through it.

Implement the RLEIterator class:

RLEIterator(int[] encoded) Initializes the object with the encoded array encoded.
int next(int n) Exhausts the next n elements and returns the last element exhausted in this way. If there is no element left to exhaust, return -1 instead.


Example 1:

Input
["RLEIterator", "next", "next", "next", "next"]
[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
Output
[null, 8, 8, 5, -1]

Explanation
RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // This maps to the sequence [8,8,8,5,5].
rLEIterator.next(2); // exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].
rLEIterator.next(1); // exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].
rLEIterator.next(1); // exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].
rLEIterator.next(2); // exhausts 2 terms, returning -1. This is because the first term exhausted was 5,
but the second term did not exist. Since the last term exhausted does not exist, we return -1.


Constraints:

2 <= encoding.length <= 1000
encoding.length is even.
0 <= encoding[i] <= 109
1 <= n <= 109
At most 1000 calls will be made to next.
"""
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# 40 ms
# Beats
# 84.26%
# Memory
# 14.6 MB
# Beats
# 6.77%
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.position = 0
        self.value = 0
        self.values = [[encoding[2*i+1], encoding[2*i]] for i in range(len(encoding)//2) if encoding[2*i] > 0]

    def next(self, n: int) -> int:
        while n:
            if self.position == len(self.values):
                return -1
            value = self.values[self.position][0]
            advance = min(self.values[self.position][1]-self.value, n)
            n -= advance
            self.value += advance
            if self.value == self.values[self.position][1]:
                self.value = 0
                self.position += 1
        return value

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)


tests = [
    [
        ["RLEIterator", "next", "next", "next", "next"],
        [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]],
        [null, 8, 8, 5, -1]
    ]
]

run_object_tests(tests, cls=RLEIterator)
