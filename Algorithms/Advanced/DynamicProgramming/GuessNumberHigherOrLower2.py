"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.



Example 1:


Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
Example 2:

Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
Example 3:

Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.


Constraints:

1 <= n <= 200
"""
import math
from functools import lru_cache

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def getMoneyAmount(self, n: int) -> int:
#
#         @lru_cache(None)
#         def solve(n: int) -> int:
#             if n == 0:
#                 return 0
#             if n == 1:
#                 return 0
#             if n == 2:
#                 return 1
#
#             def decide_step(n: int):
#                 Sn = n * (n+1) // 2
#                 S1 = 1
#                 St = (S1 + Sn) // 2
#                 l, r = 1, n
#                 while l < r:
#                     mid = l + (r-l) // 2
#                     Sm = (mid+1)*mid // 2
#                     if Sm < St:
#                         l = mid + 1
#                     else:
#                         r = mid
#                 return l
#             p = decide_step(n)
#             print(n, p)
#             return p + max(solve(p-1), p + solve(n-p))
#
#         return solve(n)


# Runtime: 2880 ms, faster than 71.88% of Python3 online submissions for Guess Number Higher or Lower II.
# Memory Usage: 15 MB, less than 77.91% of Python3 online submissions for Guess Number Higher or Lower II.
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/1290321/Easy-Java-sol-90-time
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for l in range(1, n+1):
            for i in range(1, n-l+1):
                j = i + l
                minv = math.inf
                for k in range(i, j):
                    val = k + max(dp[i][k-1], dp[k+1][j])
                    minv = min(minv, val)
                dp[i][j] = minv
        return dp[1][n]


tests = [
    [10, 16],
    [1, 0],
    [2, 1]
]

run_functional_tests(Solution().getMoneyAmount, tests)