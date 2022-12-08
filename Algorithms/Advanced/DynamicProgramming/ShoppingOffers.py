"""
https://leetcode.com/problems/shopping-offers/

In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.



Example 1:

Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14
Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B.
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:

Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
Output: 11
Explanation: The price of A is $2, and $3 for B, $4 for C.
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C.
You cannot add more items, though only $9 for 2A ,2B and 1C.


Constraints:

n == price.length == needs.length
1 <= n <= 6
0 <= price[i], needs[i] <= 10
1 <= special.length <= 100
special[i].length == n + 1
0 <= special[i][j] <= 50
"""
import copy
from functools import lru_cache
from typing import List

from numpy import dot

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
#         n = len(price)
#         total = sum(price*amount for price, amount in zip(price, needs))
#         gain = [offer[-1] - sum(price*amount for price, amount in zip(price, offer[:n])) for offer in special]
#         to_visit = [[needs, total]]
#         result = total
#         while to_visit:
#             current, total = to_visit.pop()
#             result = min(result, total)
#             for offer, special_gain in zip(special, gain):
#                 next_state = [ni - oi for ni, oi in zip(current, offer[:n])]
#                 if any(new_need_i < 0 for new_need_i in next_state):
#                     continue
#                 to_visit.append([next_state, total + special_gain])
#
#         return result

# TLE
# class Solution:
#     def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
#         n = len(price)
#         m = len(special)
#         total = sum(price*amount for price, amount in zip(price, needs))
#         gain = [offer[-1] - sum(price*amount for price, amount in zip(price, offer[:n])) for offer in special]
#         to_visit = [[needs, total, 0]]
#         visited = set()
#         visited.add(0)
#         result = total
#         while to_visit:
#             current, total, code = to_visit.pop()
#             result = min(result, total)
#             for offer, special_gain, j in zip(special, gain, range(m)):
#                 next_state = [ni - oi for ni, oi in zip(current, offer[:n])]
#                 if any(new_need_i < 0 for new_need_i in next_state):
#                     continue
#                 new_code = code + m ** j
#                 if new_code not in visited:
#                     visited.add(new_code)
#                     to_visit.append([next_state, total + special_gain, new_code])
#
#         return result


# class Solution:
#     def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
#         n = len(price)
#         Q = max(needs) + 1
#         M = Q ** n
#         dp = [0] * M
#         to_visit = {0}
#         while to_visit:
#

# TLE
# https://leetcode.com/problems/shopping-offers/solutions/127643/shopping-offers/
# class Solution:
#     def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
#
#         def shopping(needs):
#             result = dot(needs, price)
#             for offer in special:
#                 current_needs = copy.copy(needs)
#                 not_enough = False
#                 for j in range(len(needs)):
#                     diff = current_needs[j] - offer[j]
#                     if diff < 0:
#                         not_enough = True
#                     current_needs[j] = diff
#                 if not not_enough:
#                     result = min(result, offer[-1] + shopping(current_needs))
#             return result
#
#         return shopping(needs)


# Runtime
# 363 ms
# Beats
# 24.11%
# Memory
# 31.9 MB
# Beats
# 5.80%
# https://leetcode.com/problems/shopping-offers/solutions/127643/shopping-offers/
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        Q = max(needs)+1

        visited = dict()

        def build_hash(needs):
            nonlocal Q
            res = 0
            for ni in needs:
                res *= Q
                res += ni
            return res

        def shopping(needs):
            code = build_hash(needs)
            if code in visited:
                return visited.get(code)
            result = dot(needs, price)
            for offer in special:
                current_needs = copy.copy(needs)
                not_enough = False
                for j in range(len(needs)):
                    diff = current_needs[j] - offer[j]
                    if diff < 0:
                        not_enough = True
                    current_needs[j] = diff
                if not not_enough:
                    result = min(result, offer[-1] + shopping(current_needs))
            visited[code] = result
            return result

        return shopping(needs)


tests = [
    [[2, 2], [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,1,7],[1,1,8],[1,1,9],[1,1,10],[1,1,11],[1,1,12],[1,1,13],[1,1,14],[1,1,15]], [10, 10], 10],
    [[2,5], [[3,0,5],[1,2,10]], [3,2], 14],
    [[2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1], 11]
]

run_functional_tests(Solution().shoppingOffers, tests)
