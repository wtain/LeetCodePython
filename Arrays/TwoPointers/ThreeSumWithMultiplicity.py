"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3682/
https://leetcode.com/problems/3sum-with-multiplicity/

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""
import bisect
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 3460 ms, faster than 15.41% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14.3 MB, less than 92.48% of Python3 online submissions for 3Sum With Multiplicity.
# class Solution:
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         MOD = 10 ** 9 + 7
#         arr.sort()
#         result = 0
#         n = len(arr)
#
#         for i in range(n):
#             t1 = target - arr[i]
#             j, k = i+1, n-1
#             while j < k:
#                 if arr[j] + arr[k] > t1:
#                     k -= 1
#                 elif arr[j] + arr[k] < t1:
#                     j += 1
#                 elif arr[j] != arr[k]:
#                     cnt1, cnt2 = 1, 1
#                     while j+1 < k and arr[j] == arr[j+1]:
#                         j += 1
#                         cnt1 += 1
#                     while k-1 > j and arr[k-1] == arr[k]:
#                         k -= 1
#                         cnt2 += 1
#                     result += cnt1 * cnt2
#                     result %= MOD
#                     j += 1
#                     k -= 1
#                 else:
#                     cnt = (k-j+1)
#                     result += cnt * (cnt-1) // 2
#                     result %= MOD
#                     break
#
#         return result


# Runtime: 80 ms, faster than 71.05% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14.4 MB, less than 77.44% of Python3 online submissions for 3Sum With Multiplicity.
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        c = Counter(arr)
        arr_sorted = sorted(c.keys())
        result = 0
        n = len(arr_sorted)
        for i in range(n-2):
            for j in range(n-1, i, -1):
                v = target - arr_sorted[i] - arr_sorted[j]
                if v > arr_sorted[j]:
                    result += c[v] * c[arr_sorted[i]] * c[arr_sorted[j]]
                    result %= MOD

        for i in range(n-1):
            v = target - 2 * arr_sorted[i]
            if v > arr_sorted[i]:
                result += c[v] * c[arr_sorted[i]] * (c[arr_sorted[i]]-1) // 2
                result %= MOD

        for i in range(n):
            if (target - arr_sorted[i]) % 2 == 0:
                v = (target - arr_sorted[i]) // 2
                if v > arr_sorted[i]:
                    result += c[arr_sorted[i]] * c[v] * (c[v] - 1) // 2
                    result %= MOD

        if target % 3 == 0:
            v = target // 3
            result += c[v] * (c[v] - 1) * (c[v] - 2) // 6
            result %= MOD

        return result



tests = [
    ([1,1,2,2,3,3,4,4,5,5], 8, 20),
    ([1,1,2,2,2,2], 5, 12)
]

run_functional_tests(Solution().threeSumMulti, tests)