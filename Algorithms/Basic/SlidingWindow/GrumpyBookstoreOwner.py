"""
https://leetcode.com/problems/grumpy-bookstore-owner/

Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""
from typing import List


# Runtime: 268 ms, faster than 98.35% of Python3 online submissions for Grumpy Bookstore Owner.
# Memory Usage: 16.4 MB, less than 74.05% of Python3 online submissions for Grumpy Bookstore Owner.
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        result = 0
        n = len(customers)
        for i in range(X):
            result += customers[i]
        for i in range(X, n):
            if not grumpy[i]:
                result += customers[i]
        current = result
        for i in range(X, n):
            l = i - X
            if grumpy[l]:
                current -= customers[l]
            if grumpy[i]:
                current += customers[i]
            result = max(result, current)
        return result


tests = [
    ([4,10,10], [1,1,0], 2, 24),

    ([3], [1], 1, 3),

    ([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3, 16)
]

run_functional_tests(Solution().maxSatisfied, tests)
