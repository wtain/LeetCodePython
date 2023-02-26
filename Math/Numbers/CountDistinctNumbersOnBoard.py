"""
https://leetcode.com/problems/count-distinct-numbers-on-board/

You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:

For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
Then, place those numbers on the board.
Return the number of distinct integers present on the board after 109 days have elapsed.

Note:

Once a number is placed on the board, it will remain on it until the end.
% stands for the modulo operation. For example, 14 % 3 is 2.


Example 1:

Input: n = 5
Output: 4
Explanation: Initially, 5 is present on the board.
The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1.
After that day, 3 will be added to the board because 4 % 3 == 1.
At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5.
Example 2:

Input: n = 3
Output: 2
Explanation:
Since 3 % 2 == 1, 2 will be added to the board.
After a billion days, the only two distinct numbers on the board are 2 and 3.


Constraints:

1 <= n <= 100
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 47 ms
# Beats
# 21.28%
# Memory
# 13.9 MB
# Beats
# 42.85%
# class Solution:
#     def distinctIntegers(self, n: int) -> int:
#         to_visit = {n}
#         visited = set()
#         while to_visit:
#             x = to_visit.pop()
#             visited.add(x)
#             for i in range(2, n):
#                 if x % i == 1 and i not in visited and i not in to_visit:
#                     to_visit.add(i)
#         return len(visited)


# Runtime
# 25 ms
# Beats
# 94.49%
# Memory
# 13.8 MB
# Beats
# 42.85%
# https://leetcode.com/problems/count-distinct-numbers-on-board/solutions/3111605/python-one-liner-solution/
class Solution:
    def distinctIntegers(self, n: int) -> int:
        return [n-1, 1][n == 1]


tests = [
    [5, 4],
    [3, 2],
]

run_functional_tests(Solution().distinctIntegers, tests)
