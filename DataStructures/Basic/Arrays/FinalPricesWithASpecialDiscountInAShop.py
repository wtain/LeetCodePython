"""
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.



Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation:
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.
Example 2:

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.
Example 3:

Input: prices = [10,1,1,6]
Output: [9,0,1,6]


Constraints:

1 <= prices.length <= 500
1 <= prices[i] <= 10^3
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 17.28% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
# Memory Usage: 14.3 MB, less than 79.86% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         n = len(prices)
#         result = prices.copy()
#         for i in range(n):
#             for j in range(i+1, n):
#                 if prices[j] <= prices[i]:
#                     result[i] -= prices[j]
#                     break
#         return result


# Runtime: 52 ms, faster than 70.75% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
# Memory Usage: 14.2 MB, less than 79.86% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = prices.copy()
        st = []
        for i in range(n):
            while st and prices[i] <= prices[st[-1]]:
                result[st[-1]] -= prices[i]
                st.pop()
            st.append(i)
        return result


tests = [
    [[8,4,6,2,3], [4,2,4,2,3]],
    [[1,2,3,4,5], [1,2,3,4,5]],
    [[10,1,1,6], [9,0,1,6]]
]

run_functional_tests(Solution().finalPrices, tests)