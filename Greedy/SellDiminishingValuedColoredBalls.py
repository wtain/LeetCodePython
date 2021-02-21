"""
https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.



Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.


Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)
"""
import heapq
from typing import List


## TLE
# class Solution:
#     def maxProfit(self, inventory: List[int], orders: int) -> int:
#         MOD = 10**9+7
#         result = 0
#         h = [(-i, i) for i in inventory]
#         heapq.heapify(h)
#         while orders > 0:
#             _, cnt = heapq.heappop(h)
#             next = 0
#             if h:
#                 next = h[0][1]
#             nuse = min(orders, cnt-next+1)
#             result += (cnt + cnt-nuse+1) * nuse // 2
#             # print(cnt, cnt-nuse+1)
#             result %= MOD
#             cnt -= nuse
#             if cnt > 0:
#                 heapq.heappush(h, (-cnt, cnt))
#             orders -= nuse
#         return result

# Runtime: 712 ms, faster than 74.13% of Python3 online submissions for Sell Diminishing-Valued Colored Balls.
# Memory Usage: 24.7 MB, less than 62.19% of Python3 online submissions for Sell Diminishing-Valued Colored Balls.
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9+7
        result = 0
        inventory.sort()
        n = len(inventory)
        mult = 1
        for i in range(n-1,-1,-1):
            cnt = inventory[i]
            next = 0
            if i > 0:
                next = inventory[i-1]
            diff = (inventory[i] - next) * mult

            if diff >= orders:
                t = orders // mult
                m = orders % mult
                x = (cnt + cnt-t+1)*t*mult//2 + (cnt-t)*m
                result += x
                break
            else:
                orders -= diff
                result += (cnt+next+1)*(cnt-next)*mult//2
            mult += 1
        return result % MOD



tests = [
    ([497978859,167261111,483575207,591815159], 836556809, 373219333),

    ([2,5], 4, 14),
    ([3,5], 6, 19),
    ([2,8,4,10,6], 20, 110),
    ([1000000000], 1000000000, 21)
]

for test in tests:
    result = Solution().maxProfit(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))