"""
https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.



Example 1:

Input: price = [13,5,1,8,21,2], k = 3
Output: 8
Explanation: Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.
Example 2:

Input: price = [1,3,1], k = 2
Output: 2
Explanation: Choose the candies with the prices [1,3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.
Example 3:

Input: price = [7,7,7,7], k = 2
Output: 0
Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0.


Constraints:

2 <= k <= price.length <= 105
1 <= price[i] <= 109
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maximumTastiness(self, price: List[int], k: int) -> int:
#         price.sort()
#         vmin, vmax = price[0], price[-1]
#         med = (vmin+vmax) // 2
#         index = bisect.bisect_left(price, med, 1, len(price)-1)
#         return min(price[index]-vmin, vmax-price[index])


# Runtime
# 5286 ms
# Beats
# 5.4%
# Memory
# 26 MB
# Beats
# 35.8%
# # https://leetcode.com/problems/maximum-tastiness-of-candy-basket/solutions/2948016/binary-search-nlogn-easy-to-understand/
# class Solution:
#     def maximumTastiness(self, price: List[int], k: int) -> int:
#         price.sort()
#         n = len(price)
#         s, e = 0, price[-1] - price[0]
#
#         def check(m: int) -> bool:
#             nonlocal price, n, k
#             if price[-1] - price[0] < m:
#                 return False
#             cnt, pre = 1, price[0]
#             for i in range(1, n):
#                 if price[i] - pre >= m:
#                     pre = price[i]
#                     cnt += 1
#
#             return cnt >= k
#
#         while e - s > 1:
#             m = (s+e) // 2
#             if check(m):
#                 s = m
#             else:
#                 e = m-1
#         return e if check(e) else s


# Runtime
# 1731 ms
# Beats
# 52.52%
# Memory
# 26 MB
# Beats
# 35.8%
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/solutions/2948016/binary-search-nlogn-easy-to-understand/
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        s, e = 0, price[-1] - price[0]

        def check(m: int) -> bool:
            nonlocal price, n, k
            if price[-1] - price[0] < m:
                return False
            cnt, pre = 1, price[0]
            for i in range(1, n):
                if price[i] - pre >= m:
                    pre = price[i]
                    cnt += 1
                    if cnt == k:
                        return True

            return cnt >= k

        while e - s > 1:
            m = (s+e) // 2
            if check(m):
                s = m
            else:
                e = m-1
        return e if check(e) else s


tests = [
    [[13,5,1,8,21,2], 3, 8],
    [[1,3,1], 2, 2],
    [[7,7,7,7], 2, 0]
]

run_functional_tests(Solution().maximumTastiness, tests)
