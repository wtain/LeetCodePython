"""
https://leetcode.com/problems/can-make-palindrome-from-substring/

You are given a string s and array queries where queries[i] = [lefti, righti, ki]. We may rearrange the substring s[lefti...righti] for each query and then choose up to ki of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

Return a boolean array answer where answer[i] is the result of the ith query queries[i].

Note that each letter is counted individually for replacement, so if, for example s[lefti...righti] = "aaa", and ki = 2, we can only replace two of the letters. Also, note that no query modifies the initial string s.



Example :

Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0]: substring = "d", is palidrome.
queries[1]: substring = "bc", is not palidrome.
queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
Example 2:

Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
Output: [false,true]


Constraints:

1 <= s.length, queries.length <= 105
0 <= lefti <= righti < s.length
0 <= ki <= s.length
s consists of lowercase English letters.
"""
from typing import List

from Common.Constants import false, true
from Common.ObjectTestingUtils import run_functional_tests


# Naive, TLE expected for 10^5 * 10^5
# class Solution:
#     def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
#         result = []
#         for i1, i2, k in queries:
#             mismatches = 0
#             is_palindrome = True
#             while i1 < i2:
#                 if s[i1] != s[i2]:
#                     mismatches += 1
#                     if mismatches > k:
#                         is_palindrome = False
#                         break
#                 i1 += 1
#                 i2 -= 1
#             result.append(is_palindrome)
#         return result


# class Solution:
#     def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
#         n = len(s)
#         hash1 = [0] * n
#         hash2 = [0] * n
#
#         def char_hash(c):
#             return ord(c) - ord('a')  # 0..25
#
#         def char_hash1(c):
#             return 27 - char_hash(c)  # 1..26
#
#         def char_hash2(c):
#             return 27 + char_hash(c)  # 27..53
#
#         MUL = 100
#
#         hash1[0] = char_hash1(s[0])
#         for i in range(1, n):
#             hash1[i] = MUL * hash1[i-1] + char_hash1(s[i])
#
#         hash2[-1] = char_hash2(s[-1])  # 28..53
#         for i in range(n-2, -1, -1):
#             hash2[i] = MUL * hash2[i + 1] + char_hash2(s[i])
#
#         print(hash1)
#         print(hash2)
#
#         def calc_hash1(i1, i2):
#             h1 = hash1[i2]
#             if i1 > 0:
#                 h1 -= hash1[i1 - 1] * (MUL ** (i2-i1+1))
#                 h1 //= MUL ** i1
#             return h1
#
#         def calc_hash2(i1, i2):
#             h2 = hash2[i1]
#             if i2 < n - 1:
#                 h2 -= hash2[i2 + 1] * (MUL ** (i2-i1+1))
#                 h2 //= MUL ** (n - i2 - 1)
#             return h2
#
#         result = []
#         for i1, i2, k in queries:
#             h1 = calc_hash1(i1, i2)
#             h2 = calc_hash2(i1, i2)
#
#             diff0 = diff = h2 + h1
#             mismatches = 0
#             # while diff:
#             for i in range(i1, i2+1):
#                 if diff % MUL != 54:
#                     mismatches += 1
#                 diff //= MUL
#             # result.append(mismatches <= 2*k and n % 2 == 1 or mismatches <= k)
#             # print(mismatches)
#             print(s[i1:i2 + 1], h1, h2, diff0, mismatches)
#             result.append(mismatches <= 2 * k)
#
#         return result


# c0c1c2...c(i-1)c(i)c(i+1)...c(n-1)

# hash1(i) = hash(c0...ci)     => hash(ci...cj) = (hash1(j) - hash1(i-1)) << i
# hash2(i) = hash(ci...c(n-1)) => similar...
# query(i, j, k) = hash1(i..j) - hash2(i..j)
# abc =>  hash(abc) = 0*26^2 + 1 * 26 + 2
#         hash(cba) = 2*26^2 + 1 * 26 + 0
# h1 - h2 = -3 * 26^2 + 2
# 26 -> 52: for hash1: 0..25, for hash2 - 26..51
# abc =>  hash(abc) = 0*52^2 + 1 * 52 + 2
#         hash(cba) = 28*52^2 + 27 * 52 + 26
# h2 - h1 = 28 * 52^2 + 26 * 52 + 28
# mod mod 26 = 2


# Runtime
# 2327 ms
# Beats
# 54.55%
# Memory
# 63.2 MB
# Beats
# 74.83%
# https://leetcode.com/problems/can-make-palindrome-from-substring/solutions/2846031/python-3-9-10-lines-xor-three-versions-t-m-99-94/
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        d, result = [[0] * 26], []
        for c in s:
            nx = d[-1].copy()
            nx[ord(c) - 97] ^= 1
            d.append(nx)
        for l, r, k in queries:
            odds = sum(d[l][i] ^ d[r+1][i] for i in range(26))
            result.append(odds //2 <= k)
        return result


tests = [
    ["abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]], [true,false,false,true,true]],
    ["lyb", [[0,1,0],[2,2,1]], [false,true]],
    ["ninmjmj", [[6,6,0],[1,1,1],[2,5,4],[1,3,1],[5,6,1]], [true,true,true,true,true]],
]

run_functional_tests(Solution().canMakePaliQueries, tests)
