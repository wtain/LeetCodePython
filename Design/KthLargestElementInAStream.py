"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""
import heapq
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests

# Runtime: 92 ms, faster than 98.12% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.4 MB, less than 31.19% of Python3 online submissions for Kth Largest Element in a Stream.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxes = []
        for v in nums:
            self.add(v)

    def add(self, val: int) -> int:
        if len(self.maxes) == self.k:
            if self.maxes[0] < val:
                heapq.heappop(self.maxes)
                heapq.heappush(self.maxes, val)
        else:
            heapq.heappush(self.maxes, val)
        return self.maxes[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


tests = [
    [
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
        [null, 4, 5, 5, 8, 8]
    ]
]

run_object_tests(tests, cls=KthLargest)
