"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/?envType=daily-question&envId=2024-07-08

There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.



Example 1:


Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
Example 2:

Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.


Constraints:

1 <= k <= n <= 500


Follow up:

Could you solve this problem in linear time with constant space?
"""
from collections import deque

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         present = [True] * n
#         cnt = n
#         pos = -1
#         while cnt > 1:
#             pos += k
#             pos %= n
#             while not present[pos]:
#                 pos += 1
#                 pos %= n
#             present[pos] = False
#             cnt -= 1
#             while not present[pos]:
#                 pos += 1
#                 pos %= n
#         for i in range(n):
#             if present[i]:
#                 return i
#         return -1


# Runtime
# 40
# ms
# Beats
# 54.75%
# Analyze Complexity
# Memory
# 16.78
# MB
# Beats
# 8.19%
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/editorial/?envType=daily-question&envId=2024-07-08
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         circle = list(range(1, n+1))
#         start = 0
#         while len(circle) > 1:
#             removal = (start+k-1) % len(circle)
#             circle.pop(removal)
#             start = removal
#
#         return circle[0]


# Runtime
# 116
# ms
# Beats
# 28.12%
# Analyze Complexity
# Memory
# 16.49
# MB
# Beats
# 84.30%
# Analyze
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/editorial/?envType=daily-question&envId=2024-07-08
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         circle = deque(range(1, n+1))
#         while len(circle) > 1:
#             for _ in range(k-1):
#                 circle.append(circle.popleft())
#             circle.popleft()
#
#         return circle[0]

# Runtime
# 37
# ms
# Beats
# 70.20%
# Analyze Complexity
# Memory
# 16.51
# MB
# Beats
# 49.47%
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/editorial/?envType=daily-question&envId=2024-07-08
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         def impl(n, k):
#             if n == 1:
#                 return 0
#             return (impl(n-1, k) + k) % n
#         return impl(n, k) + 1


# Runtime
# 30
# ms
# Beats
# 93.48%
# Analyze Complexity
# Memory
# 16.54
# MB
# Beats
# 49.47%
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/editorial/?envType=daily-question&envId=2024-07-08
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0
        for i in range(2, n+1):
            result = (result + k) % i
        return result+1



tests = [
    [5, 2, 3],
    [6, 5, 1],
]

run_functional_tests(Solution().findTheWinner, tests)
