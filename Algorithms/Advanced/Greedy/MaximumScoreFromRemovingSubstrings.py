"""
https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2024-07-12

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.



Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20


Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 249
# ms
# Beats
# 66.88%
# Analyze Complexity
# Memory
# 18.28
# MB
# Beats
# 49.35%
# https://leetcode.com/problems/maximum-score-from-removing-substrings/editorial/?envType=daily-question&envId=2024-07-12
# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         total = 0
#         high_priority_pair = "ab" if x > y else "ba"
#         low_priority_pair = "ba" if high_priority_pair == "ab" else "ab"
#
#         string_after_1 = self.remove_substr(s, high_priority_pair)
#         removed_count = (len(s) - len(string_after_1)) // 2
#
#         total += removed_count * max(x, y)
#
#         string_after_2 = self.remove_substr(string_after_1, low_priority_pair)
#         removed_count = (len(string_after_1) - len(string_after_2)) // 2
#
#         total += removed_count * min(x, y)
#         return total
#
#     def remove_substr(self, input, target):
#         st = []
#         for c in input:
#             if c == target[1] and st and st[-1] == target[0]:
#                 st.pop()
#             else:
#                 st.append(c)
#
#         return "".join(st)


# Runtime
# 381
# ms
# Beats
# 36.36%
# Analyze Complexity
# Memory
# 18.36
# MB
# Beats
# 38.96%
# https://leetcode.com/problems/maximum-score-from-removing-substrings/editorial/?envType=daily-question&envId=2024-07-12
# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         total = 0
#         s = list(s)
#
#         if x > y:
#             total += self.remove_substring(s, "ab", x)
#             total += self.remove_substring(s, "ba", y)
#         else:
#             total += self.remove_substring(s, "ba", y)
#             total += self.remove_substring(s, "ab", x)
#         return total
#
#     def remove_substring(self, s, t, p):
#         total, w = 0, 0
#
#         for r in range(len(s)):
#             s[w] = s[r]
#             w += 1
#
#             if w > 1 and s[w-2] == t[0] and s[w-1] == t[1]:
#                 w -= 2
#                 total += p
#
#         del s[w:]
#         return total


# Runtime
# 218
# ms
# Beats
# 79.22%
# Analyze Complexity
# Memory
# 17.39
# MB
# Beats
# 81.82%
# https://leetcode.com/problems/maximum-score-from-removing-substrings/editorial/?envType=daily-question&envId=2024-07-12
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x, y = y, x

        ac, bc, t = 0, 0, 0

        for i in range(len(s)):
            if s[i] == "a":
                ac += 1
            elif s[i] == 'b':
                if ac > 0:
                    ac -= 1
                    t += x
                else:
                    bc += 1
            else:
                t += min(ac, bc) * y
                ac = bc = 0
        t += min(ac, bc) * y

        return t


tests = [
    ["cdbcbbaaabab", 4, 5, 19],
    ["aabbaaxybbaabb", 5, 4, 20],
]

run_functional_tests(Solution().maximumGain, tests)
