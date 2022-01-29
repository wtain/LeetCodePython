"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3737/
https://leetcode.com/problems/construct-target-array-with-multiple-sums/

Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.



Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1]
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true


Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9

Given that the sum is strictly increasing, the largest element in the target must be formed in the last step by adding the total sum in the previous step. Thus, we can simulate the process in a reversed way.

Subtract the largest with the rest of the array, and put the new element into the array. Repeat until all elements become one
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Straightforward (without heap)
# class Solution:
#     def isPossible(self, target: List[int]) -> bool:
#         n = len(target)
#         s = sum(target)
#         n1 = sum(map(lambda x: x == 1, target))
#         while n1 < n:
#             # print(target, s)
#             index, value = max(enumerate(target), key=operator.itemgetter(1))
#             s -= target[index]
#             target[index] -= s
#             s += target[index]
#             if target[index] < 1:
#                 return False
#             elif target[index] == 1:
#                 n1 += 1
#         return True


# Runtime: 292 ms, faster than 16.79% of Python3 online submissions for Construct Target Array With Multiple Sums.
# Memory Usage: 22.6 MB, less than 6.57% of Python3 online submissions for Construct Target Array With Multiple Sums.
# class Solution:
#     def isPossible(self, target: List[int]) -> bool:
#         n = len(target)
#         s = sum(target)
#         n1 = sum(map(lambda x: x == 1, target))
#         # h = target.copy()
#         h = [(-t, i) for i, t in enumerate(target)]
#         heapq.heapify(h)
#         while n1 < n:
#             # print(target, s)
#             # index, value = max(enumerate(target), key=operator.itemgetter(1))
#             _, index = heapq.heappop(h)
#             s -= target[index]
#
#             if s == 0:
#                 return False
#
#             r = 1
#             if len(h) >= 1:
#                 nextv = -h[0][0]
#                 diff = target[index] - nextv
#                 r1 = diff // s
#                 if r1 > 1:
#                     r = r1
#
#             target[index] -= r * s
#
#             heapq.heappush(h, (-target[index], index))
#             s += target[index]
#             if target[index] < 1:
#                 return False
#             elif target[index] == 1:
#                 n1 += 1
#         return True


# Runtime: 252 ms, faster than 74.45% of Python3 online submissions for Construct Target Array With Multiple Sums.
# Memory Usage: 20.2 MB, less than 26.28% of Python3 online submissions for Construct Target Array With Multiple Sums.
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        h = [-x for x in target]
        s = sum(target)
        heapq.heapify(h)
        while h[0] != -1:
            x = - heapq.heappop(h)
            s -= x
            if x <= s or s < 1:
                return False
            x %= s
            s += x
            heapq.heappush(h, -x)
        return True


tests = [
    [[2], False],

    [[1,1000000000], True],

    [[9,3,5], True],
    [[1,1,1,2], False],
    [[8,5], True]
]

run_functional_tests(Solution().isPossible, tests)