"""
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2023-11-28

Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.



Example 1:


Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.
Example 2:


Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.
Example 3:


Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.


Constraints:

n == corridor.length
1 <= n <= 105
corridor[i] is either 'S' or 'P'.
"""
from Common.ObjectTestingUtils import run_functional_tests

# Runtime
# 3932
# ms
# Beats
# 5.71%
# of users with Python3
# Memory
# 134.92
# MB
# Beats
# 5.71%
# of users with Python3
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/editorial/?envType=daily-question&envId=2023-11-28
# class Solution:
#     def numberOfWays(self, corridor: str) -> int:
#         MOD = 10 ** 9 + 7
#         cache = [[-1] * 3 for _ in range(len(corridor))]
#
#         def count(index, seats):
#             if index == len(corridor):
#                 return 1 if seats == 2 else 0
#
#             if cache[index][seats] != -1:
#                 return cache[index][seats]
#
#             if seats == 2:
#                 if corridor[index] == 'S':
#                     result = count(index + 1, 1)
#                 else:
#                     result = (count(index+1, 0) + count(index+1, 2)) % MOD
#             else:
#                 if corridor[index] == 'S':
#                     result = count(index+1, seats+1)
#                 else:
#                     result = count(index+1, seats)
#             cache[index][seats] = result
#             return cache[index][seats]
#         return count(0, 0)


# Runtime
# 1948
# ms
# Beats
# 7.14%
# of users with Python3
# Memory
# 30.53
# MB
# Beats
# 12.86%
# of users with Python3
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/editorial/?envType=daily-question&envId=2023-11-28
# class Solution:
#     def numberOfWays(self, corridor: str) -> int:
#         MOD = 10 ** 9 + 7
#         count = [[-1] * 3 for _ in range(len(corridor)+1)]
#         count[-1][0] = 0
#         count[-1][1] = 0
#         count[-1][2] = 1
#
#         for index in range(len(corridor)-1, -1, -1):
#             if corridor[index] == 'S':
#                 count[index][0] = count[index+1][1]
#                 count[index][1] = count[index+1][2]
#                 count[index][2] = count[index+1][1]
#             else:
#                 count[index][0] = count[index + 1][0]
#                 count[index][1] = count[index + 1][1]
#                 count[index][2] = (count[index + 1][0] + count[index+1][2]) % MOD
#         return count[0][0]


# Runtime
# 292
# ms
# Beats
# 98.57%
# of users with Python3
# Memory
# 17.30
# MB
# Beats
# 71.43%
# of users with Python3
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/editorial/?envType=daily-question&envId=2023-11-28
# class Solution:
#     def numberOfWays(self, corridor: str) -> int:
#         MOD = 10 ** 9 + 7
#         zero = 0
#         one = 0
#         two = 1
#
#         for thing in corridor:
#             if thing == 'S':
#                 zero = one
#                 one, two = two, one
#             else:
#                 two = (two + zero) % MOD
#         return zero


# Runtime
# 435
# ms
# Beats
# 54.28%
# of users with Python3
# Memory
# 21.21
# MB
# Beats
# 21.43%
# of users with Python3
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/editorial/?envType=daily-question&envId=2023-11-28
# class Solution:
#     def numberOfWays(self, corridor: str) -> int:
#         MOD = 10 ** 9 + 7
#         indices = []
#         for i, thing in enumerate(corridor):
#             if thing == 'S':
#                 indices.append(i)
#         if indices == [] or len(indices) % 2 == 1:
#             return 0
#         count = 1
#         previous_pair_last = 1
#         current_pait_first = 2
#         while current_pait_first < len(indices):
#             count *= (indices[current_pait_first] - indices[previous_pair_last])
#             count %= MOD
#             previous_pair_last += 2
#             current_pait_first += 2
#         return count


# Runtime
# 368
# ms
# Beats
# 81.43%
# of users with Python3
# Memory
# 17.37
# MB
# Beats
# 71.43%
# of users with Python3
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/editorial/?envType=daily-question&envId=2023-11-28
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        count = 1
        seats = 0
        previous_pair_last = None

        for index, thing in enumerate(corridor):
            if thing == 'S':
                seats += 1
                if seats == 2:
                    previous_pair_last = index
                    seats = 0
                elif seats == 1 and previous_pair_last is not None:
                    count *= (index - previous_pair_last)
                    count %= MOD

        if seats == 1 or previous_pair_last is None:
            return 0

        return count


tests = [
    ["SSPPSPS", 3],
    ["PPSPSP", 1],
    ["S", 0],
    ["SSPSSPSSSPPSPSPPS", 8],
]

run_functional_tests(Solution().numberOfWays, tests)
