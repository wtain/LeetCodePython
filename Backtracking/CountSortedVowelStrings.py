"""
https://leetcode.com/problems/count-sorted-vowel-strings/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3607/
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.



Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045


Constraints:

1 <= n <= 50
"""

# Runtime: 4412 ms, faster than 17.17% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.3 MB, less than 57.36% of Python3 online submissions for Count Sorted Vowel Strings.
# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#
#         def countImpl(n: int, m: int) -> int:
#             if n == 1:
#                 return m
#             res = 0
#             for i in range(1, m+1):
#                 res += countImpl(n-1, i)
#             return res
#
#         return countImpl(n, 5)

# Runtime: 44 ms, faster than 27.38% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.3 MB, less than 57.36% of Python3 online submissions for Count Sorted Vowel Strings.
# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#
#         dp = [[0] * 5 for i in range(n)]
#
#         for m in range(5):
#             dp[0][m] = m+1
#
#         for li in range(1, n):
#             l = li + 1
#             for mi in range(5):
#                 m = mi + 1
#                 v = 0
#                 for m1 in range(0, mi+1):
#                     v += dp[li-1][m1]
#                 dp[li][mi] = v
#
#         return dp[n-1][5-1]


# Runtime: 36 ms, faster than 37.32% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.3 MB, less than 57.36% of Python3 online submissions for Count Sorted Vowel Strings.
# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         return (n+1) * (n+2) * (n+3) * (n+4) // 24

# Runtime: 56 ms, faster than 23.66% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.3 MB, less than 57.36% of Python3 online submissions for Count Sorted Vowel Strings.
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(5):
            for j in range(1, n+1):
                dp[j] += dp[j-1]
        return dp[n]



tests = [
    (1, 5),
    (2, 15),
    (33, 66045)
]

for test in tests:
    result = Solution().countVowelStrings(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))