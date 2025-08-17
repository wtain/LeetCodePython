"""
https://leetcode.com/problems/distribute-money-to-maximum-children/description/

You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.



Example 1:

Input: money = 20, children = 3
Output: 1
Explanation:
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child.
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
Example 2:

Input: money = 16, children = 2
Output: 2
Explanation: Each child can be given 8 dollars.


Constraints:

1 <= money <= 200
2 <= children <= 30
"""
from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def distMoney(self, money: int, children: int) -> int:
#         base = money // children
#         remainder = money % children
#         if base == 8:
#             if remainder == 0:
#                 return children
#             else:
#                 return children-1
#         if base < 4:
#         return 0

"""
Runtime
4
ms
Beats
26.76%
Analyze Complexity
Memory
17.83
MB
Beats
47.32%
"""
# https://leetcode.com/problems/distribute-money-to-maximum-children/solutions/3312090/ugh-o-1/
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        if money // 7 == children and money % 7 == 0:
            return children
        if money // 7 == children-1 and money % 7 == 3:
            return children - 2
        return min(children - 1, money // 7)


tests = [
    [2, 2, 0],
    [20, 3, 1],
    [16, 2, 2],
]

run_functional_tests(Solution().distMoney, tests)
