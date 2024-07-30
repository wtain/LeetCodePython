"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2024-07-30

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.



Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.


Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
"""
from Common.ObjectTestingUtils import run_functional_tests


# untime
# 650
# ms
# Beats
# 18.34%
# Analyze Complexity
# Memory
# 22.18
# MB
# Beats
# 16.33%
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/editorial/?envType=daily-question&envId=2024-07-30
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         n = len(s)
#         count_a = [0] * n
#         count_b = [0] * n
#         b_count = 0
#
#         for i in range(n):
#             count_b[i] = b_count
#             if s[i] == 'b':
#                 b_count += 1
#
#         a_count = 0
#         for i in range(n-1, -1, -1):
#             count_a[i] = a_count
#             if s[i] == 'a':
#                 a_count += 1
#
#         min_deletions = n
#         for i in range(n):
#             min_deletions = min(min_deletions, count_a[i] + count_b[i])
#         return min_deletions


# Runtime
# 565
# ms
# Beats
# 28.00%
# Analyze Complexity
# Memory
# 20.03
# MB
# Beats
# 32.33%
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/editorial/?envType=daily-question&envId=2024-07-30
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         n = len(s)
#         count_a = [0] * n
#
#         a_count = 0
#         for i in range(n-1, -1, -1):
#             count_a[i] = a_count
#             if s[i] == 'a':
#                 a_count += 1
#
#         min_deletions = n
#         b_count = 0
#         for i in range(n):
#             min_deletions = min(min_deletions, count_a[i] + b_count)
#             if s[i] == 'b':
#                 b_count += 1
#         return min_deletions


# Runtime
# 481
# ms
# Beats
# 36.34%
# Analyze Complexity
# Memory
# 17.64
# MB
# Beats
# 79.00%
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/editorial/?envType=daily-question&envId=2024-07-30
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         n = len(s)
#         a_count = sum(1 for ch in s if ch == 'a')
#         b_count = 0
#         min_deletions = n
#         for ch in s:
#             if ch == 'a':
#                 a_count -= 1
#             min_deletions = min(min_deletions, a_count + b_count)
#             if ch == 'b':
#                 b_count += 1
#         return min_deletions


# Runtime
# 230
# ms
# Beats
# 86.00%
# Analyze Complexity
# Memory
# 17.92
# MB
# Beats
# 40.00%
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/editorial/?envType=daily-question&envId=2024-07-30
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         char_stack = []
#         delete_count = 0
#
#         for char in s:
#             if char_stack and char_stack[-1] == 'b' and char == 'a':
#                 char_stack.pop()
#                 delete_count += 1
#             else:
#                 char_stack.append(char)
#         return delete_count


# Runtime
# 362
# ms
# Beats
# 54.00%
# Analyze Complexity
# Memory
# 20.29
# MB
# Beats
# 23.00%
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/editorial/?envType=daily-question&envId=2024-07-30
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         n = len(s)
#         dp = [0] * (n+1)
#         b_count = 0
#         for i in range(n):
#             if s[i] == 'b':
#                 dp[i+1] = dp[i]
#                 b_count += 1
#             else:
#                 dp[i+1] = min(dp[i]+1, b_count)
#
#         return dp[n]


# Runtime
# 234
# ms
# Beats
# 85.33%
# Analyze Complexity
# Memory
# 17.78
# MB
# Beats
# 66.67%
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/editorial/?envType=daily-question&envId=2024-07-30
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        min_deletions = 0
        b_count = 0
        for ch in s:
            if ch == 'b':
                b_count += 1
            else:
                min_deletions = min(min_deletions+1, b_count)

        return min_deletions


tests = [
    ["aababbab", 2],
    ["bbaaaaabb", 2],
]

run_functional_tests(Solution().minimumDeletions, tests)
