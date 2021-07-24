"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3810/
https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import heapq

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 196 ms, faster than 66.13% of Python3 online submissions for Find Median from Data Stream.
# Memory Usage: 25.6 MB, less than 43.00% of Python3 online submissions for Find Median from Data Stream.
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h_low = []
        self.h_high = []

    def addNum(self, num: int) -> None:
        if len(self.h_low) == 0:
            heapq.heappush(self.h_low, -num)
            return
        if -self.h_low[0] >= num:
            if len(self.h_low) > len(self.h_high):
                heapq.heappush(self.h_low, -num)
                n1 = -heapq.heappop(self.h_low)
                heapq.heappush(self.h_high, n1)
            else:
                heapq.heappush(self.h_low, -num)
        else:
            heapq.heappush(self.h_high, num)
            if len(self.h_high) > len(self.h_low):
                n2 = heapq.heappop(self.h_high)
                heapq.heappush(self.h_low, -n2)
        #
        # print(self.h_low)
        # print(self.h_high)

    def findMedian(self) -> float:
        if len(self.h_low) == 0:
            return 0.0
        if len(self.h_low) == len(self.h_high):
            return (-self.h_low[0] + self.h_high[0]) / 2.0
        return -self.h_low[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


tests = [
    [
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [], [3], []],
        [null, null, null, 1.5, null, 2.0]
    ],
    [
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian", "addNum", "addNum", "addNum", "findMedian"],
        [[], [1], [2], [], [3], [], [4], [5], [6], []],
        [null, null, null, 1.5, null, 2.0, null, null, null, 3.5]
    ]
]

run_object_tests(tests, cls=MedianFinder)