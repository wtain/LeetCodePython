"""
https://leetcode.com/problems/airplane-seat-assignment-probability/

n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:

Take their own seat if it is still available,
Pick other seats randomly when they find their seat occupied
What is the probability that the n-th person can get his own seat?



Example 1:

Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.
Example 2:

Input: n = 2
Output: 0.50000
Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).


Constraints:

1 <= n <= 10^5
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 20 ms, faster than 98.65% of Python3 online submissions for Airplane Seat Assignment Probability.
# Memory Usage: 14.2 MB, less than 64.69% of Python3 online submissions for Airplane Seat Assignment Probability.
# class Solution:
#     def nthPersonGetsNthSeat(self, n: int) -> float:
#         if n == 1:
#             return 1
#         return 1/2


# Runtime: 628 ms, faster than 5.12% of Python3 online submissions for Airplane Seat Assignment Probability.
# Memory Usage: 17.7 MB, less than 5.39% of Python3 online submissions for Airplane Seat Assignment Probability.
# class Solution:
#     def nthPersonGetsNthSeat(self, n: int) -> float:
#         dp = [0.0] * n
#         dp[0] = 1
#         if n >= 2:
#             dp[1] = 1/2
#         for i in range(2, n+1):
#             dp[i-1] = 1/i + (i-2) * dp[i-2] / i
#         return dp[n-1]


# Runtime: 32 ms, faster than 56.87% of Python3 online submissions for Airplane Seat Assignment Probability.
# Memory Usage: 14.2 MB, less than 64.69% of Python3 online submissions for Airplane Seat Assignment Probability.
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        return 0.5



tests = [
    [1, 1],
    [2, 0.5],
    [3, 0.5]
]

run_functional_tests(Solution().nthPersonGetsNthSeat, tests)