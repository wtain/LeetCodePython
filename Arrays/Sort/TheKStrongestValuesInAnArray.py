"""
https://leetcode.com/problems/the-k-strongest-values-in-an-array/

Given an array of integers arr and an integer k.

A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| > |arr[j] - m| where m is the median of the array.
If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].

Return a list of the strongest k values in the array. return the answer in any arbitrary order.

Median is the middle value in an ordered integer list. More formally, if the length of the list is n, the median is the element in position ((n - 1) / 2) in the sorted list (0-indexed).

For arr = [6, -3, 7, 2, 11], n = 5 and the median is obtained by sorting the array arr = [-3, 2, 6, 7, 11] and the median is arr[m] where m = ((5 - 1) / 2) = 2. The median is 6.
For arr = [-7, 22, 17, 3], n = 4 and the median is obtained by sorting the array arr = [-7, 3, 17, 22] and the median is arr[m] where m = ((4 - 1) / 2) = 1. The median is 3.


Example 1:

Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.
Example 2:

Input: arr = [1,1,3,5,5], k = 2
Output: [5,5]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].
Example 3:

Input: arr = [6,7,11,7,6,8], k = 5
Output: [11,8,6,6,7]
Explanation: Median is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is accepted.
Example 4:

Input: arr = [6,-3,7,2,11], k = 3
Output: [-3,11,2]
Example 5:

Input: arr = [-7,22,17,3], k = 2
Output: [22,17]


Constraints:

1 <= arr.length <= 10^5
-10^5 <= arr[i] <= 10^5
1 <= k <= arr.length
"""
import functools
import heapq
import statistics
from typing import List


# Runtime: 2733 ms, faster than 5.22% of Python3 online submissions for The k Strongest Values in an Array.
# Memory Usage: 27.8 MB, less than 75.46% of Python3 online submissions for The k Strongest Values in an Array.
# class Solution:
#     def getStrongest(self, arr: List[int], k: int) -> List[int]:
#         m = statistics.median_low(arr)
#         arr.sort(
#             key=functools.cmp_to_key(
#                 lambda x, y:
#                     -1 if abs(x-m) > abs(y-m) or abs(x-m) == abs(y-m) and x >= y else 1
#             )
#         )
#         return arr[:k]

# Runtime: 1392 ms, faster than 25.46% of Python3 online submissions for The k Strongest Values in an Array.
# Memory Usage: 28.6 MB, less than 48.77% of Python3 online submissions for The k Strongest Values in an Array.
# class Solution:
#     def getStrongest(self, arr: List[int], k: int) -> List[int]:
#         m = statistics.median_low(arr)
#         h = []
#         for a in arr:
#             heapq.heappush(h, [abs(a-m), a])
#             if len(h) > k:
#                 heapq.heappop(h)
#         return [v for o,v in h]

# Runtime: 1044 ms, faster than 64.11% of Python3 online submissions for The k Strongest Values in an Array.
# Memory Usage: 27.2 MB, less than 89.26% of Python3 online submissions for The k Strongest Values in an Array.
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        m = statistics.median_low(arr)
        arr.sort()
        result = []
        l, r = 0, len(arr)-1
        for i in range(k):
            cl = abs(arr[l]-m)
            cr = abs(arr[r]-m)
            if cr >= cl:
                result.append(arr[r])
                r -= 1
            else:
                result.append(arr[l])
                l += 1
        return result


tests = [
    ([1,2,3,4,5], 2, [5,1]),
    ([1,1,3,5,5], 2, [5,5]),
    ([6,7,11,7,6,8], 5, [11,8,6,6,7]),
    ([6,-3,7,2,11], 3, [-3,11,2]),
    ([-7,22,17,3], 2, [22,17])
]

for test in tests:
    result = Solution().getStrongest(test[0], test[1])
    if set(result) == set(test[2]):
        print("PASS")
    else:
        print("FAIL - " + str(result))