"""
https://leetcode.com/problems/time-needed-to-buy-tickets/

There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.



Example 1:

Input: tickets = [2,3,2], k = 2
Output: 6
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
Example 2:

Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.


Constraints:

n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 42.86% of Python3 online submissions for Time Needed to Buy Tickets.
# Memory Usage: 14.3 MB, less than 14.29% of Python3 online submissions for Time Needed to Buy Tickets.
# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         i, n, cnt = 0, len(tickets), 0
#         while tickets[k]:
#             while not tickets[i]:
#                 i = (i + 1) % n
#             cnt += 1
#             tickets[i] -= 1
#             i = (i + 1) % n
#         return cnt


# Runtime
# 54
# ms
# Beats
# 21.32%
# of users with Python3
# Memory
# 16.57
# MB
# Beats
# 51.83%
# of users with Python3
# https://leetcode.com/problems/time-needed-to-buy-tickets/editorial/?envType=daily-question&envId=2024-04-09
# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         n, t = len(tickets), 0
#
#         if tickets[k] == 1:
#             return k+1
#
#         while tickets[k] > 0:
#             for i in range(n):
#                 if tickets[i] != 0:
#                     tickets[i] -= 1
#                     t += 1
#
#                 if tickets[k] == 0:
#                     return t
#         return t


# Runtime
# 35
# ms
# Beats
# 92.79%
# of users with Python3
# Memory
# 16.58
# MB
# Beats
# 51.83%
# of users with Python3
# https://leetcode.com/problems/time-needed-to-buy-tickets/editorial/?envType=daily-question&envId=2024-04-09
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n, t = len(tickets), 0

        for i in range(n):
            if i <= k:
                t += min(tickets[k], tickets[i])
            else:
                t += min(tickets[k] - 1, tickets[i])
        return t


tests = [
    [[2,3,2], 2, 6],
    [[5,1,1,1], 0, 8]
]

run_functional_tests(Solution().timeRequiredToBuy, tests)
