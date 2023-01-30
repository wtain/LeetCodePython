"""
https://leetcode.com/problems/range-frequency-queries/

Design a data structure to find the frequency of a given value in a given subarray.

The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the RangeFreqQuery class:

RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).



Example 1:

Input
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
Output
[null, 1, 2]

Explanation
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.


Constraints:

1 <= arr.length <= 105
1 <= arr[i], value <= 104
0 <= left <= right < arr.length
At most 105 calls will be made to query
"""
from collections import Counter
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# 3447 ms
# Beats
# 24.86%
# Memory
# 157.8 MB
# Beats
# 9.83%
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.items = [Counter() for _ in range((2*self.n))]
        for i in range(self.n):
            self.items[self.n+i][arr[i]] = 1
        for i in range(self.n-1, -1, -1):
            left, right = i*2, i*2+1
            self.items[i] = self.items[left] + self.items[right]

    def query(self, left: int, right: int, value: int) -> int:
        result = 0
        left += self.n
        right += self.n
        while left <= right:
            if left % 2 == 1:
                result += self.items[left][value]
                left += 1
            if right % 2 == 0:
                result += self.items[right][value]
                right -= 1
            left //= 2
            right //= 2
        return result

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)


tests = [
    [
        ["RangeFreqQuery", "query", "query"],
        [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]],
        [null, 1, 2]
    ]
]

run_object_tests(tests, cls=RangeFreqQuery)
