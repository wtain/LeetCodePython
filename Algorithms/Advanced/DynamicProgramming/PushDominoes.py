"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3821/
https://leetcode.com/problems/push-dominoes/

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."


Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
"""
# from pipenv.vendor.semver import cmp

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def pushDominoes(self, dominoes: str) -> str:
#         n = len(dominoes)
#
#         def next_d(i: int) -> int:
#             while i < n and dominoes[i] == '.':
#                 i += 1
#             return i
#
#         l, r = -1, 0
#         while l < n:
#             r = next_d(r)
#
#             # "..."
#             if l == -1 and r == n:
#                 break
#             elif l == -1 and dominoes[r] == 'L':
#                 for i in range(r):
#                     dominoes[i] = 'L'
#                 l = r
#             elif l == -1 and dominoes[r] == 'R':
#                 l = r
#                 while l < n and dominoes[l] == 'R':
#                     l += 1
#             elif r == n:
#                 if dominoes[l] == 'R':
#                     for i in range(l+1, n):
#                         dominoes[i] = 'R'
#                     l = n
#                 else:
#                     l = n
#             elif dominoes[l] == 'R' and dominoes[r] == 'L':
#                 r0 = r
#                 while l < r:
#                     dominoes[l] = 'R'
#                     dominoes[r] = 'L'
#                     l += 1
#                     r -= 1
#                 l = r0
#
#         return dominoes


# Runtime: 276 ms, faster than 22.89% of Python3 online submissions for Push Dominoes.
# Memory Usage: 23.4 MB, less than 5.53% of Python3 online submissions for Push Dominoes.
# https://leetcode.com/problems/push-dominoes/solution/
# class Solution:
#     def pushDominoes(self, dominoes: str) -> str:
#
#         def cmp(a, b):
#             """Return negative if a<b, zero if a==b, positive if a>b."""
#             return (a > b) - (a < b)
#
#         n = len(dominoes)
#         symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
#         symbols = [(-1, 'L')] + symbols + [(n, 'R')]
#         result = list(dominoes)
#         for (i, x), (j, y) in zip(symbols, symbols[1:]):
#             if x == y:
#                 for k in range(i+1, j):
#                     result[k] = x
#             elif x > y: # RL
#                 for k in range(i+1, j):
#                     result[k] = '.LR'[cmp(k-i, j-k)]
#         return "".join(result)


# Runtime: 460 ms, faster than 10.79% of Python3 online submissions for Push Dominoes.
# Memory Usage: 19.8 MB, less than 28.95% of Python3 online submissions for Push Dominoes.
# https://leetcode.com/problems/push-dominoes/solution/
# class Solution:
#     def pushDominoes(self, dominoes: str) -> str:
#         n = len(dominoes)
#         force = [0] * n
#         f = 0
#         for i in range(n):
#             if dominoes[i] == 'R':
#                 f = n
#             elif dominoes[i] == 'L':
#                 f = 0
#             else:
#                 f = max(f-1, 0)
#             force[i] += f
#
#         f = 0
#         for i in range(n-1, -1, -1):
#             if dominoes[i] == 'L':
#                 f = n
#             elif dominoes[i] == 'R':
#                 f = 0
#             else:
#                 f = max(f-1, 0)
#             force[i] -= f
#
#         return "".join('.' if f == 0 else 'R' if f > 0 else 'L' for f in force)


# Runtime: 224 ms, faster than 45.26% of Python3 online submissions for Push Dominoes.
# Memory Usage: 16.2 MB, less than 77.11% of Python3 online submissions for Push Dominoes.
# https://leetcode.com/problems/push-dominoes/discuss/1352252/Python-simulate-process-explained
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        n = len(dominoes)
        n, prev, result = n, 0, ""
        for i in range(1, n):
            diff = i - prev - 1
            if dominoes[i] == '.':
                continue
            if dominoes[i] == dominoes[prev]:
                result += dominoes[i] * diff
            elif dominoes[i] == 'L' and dominoes[prev] == 'R':
                m, d = divmod(diff, 2)
                result += 'R' * m + '.' * d + "L" * m
            else:
                result += '.' * diff

            result += dominoes[i]
            prev = i

        return result[:-1]


tests = [
    ["RR.L", "RR.L"],
    [".L.R...LR..L..", "LL.RR.LLRRLL.."]
]

run_functional_tests(Solution().pushDominoes, tests)