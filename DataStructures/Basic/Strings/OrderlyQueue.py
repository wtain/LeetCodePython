"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3964/
https://leetcode.com/problems/orderly-queue/

You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.



Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation:
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation:
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".


Constraints:

1 <= k <= s.length <= 1000
s consist of lowercase English letters.
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def orderlyQueue(self, s: str, k: int) -> str:
#
#         def apply(s: str, k: int) -> str:
#             mi = 0
#             for i in range(1, k):
#                 if s[i] > s[mi]:
#                     mi = i
#             return s[:mi] + s[mi+1:] + s[mi]
#
#         new_s = apply(s, k)
#         while new_s < s:
#             s = new_s
#             new_s = apply(s, k)
#
#         return s


# WRONG
# class Solution:
#     def orderlyQueue(self, s: str, k: int) -> str:
#         c = Counter(s)
#         result = ""
#         for char in sorted(c):
#             result += char * c[char]
#         return result


# WRONG
# class Solution:
#     def orderlyQueue(self, s: str, k: int) -> str:
#
#         def apply(s: str, k: int) -> str:
#             mi = -1
#             for i in range(k):
#                 if mi == -1 or s[i] >= s[-1] and s[i] < s[mi]:
#                     mi = i
#             return s[:mi] + s[mi+1:] + s[mi]
#
#         new_s = apply(s, k)
#         while new_s < s:
#             s = new_s
#             new_s = apply(s, k)
#
#         return s

# WRONG
# class Solution:
#     def orderlyQueue(self, s: str, k: int) -> str:
#
#         def apply(s: str, k: int) -> str:
#             mi = 0
#             for i in range(k):
#                 if s[i] > s[i+1]:
#                     mi = i
#                     break
#             return s[:mi] + s[mi+1:] + s[mi]
#
#         new_s = apply(s, k)
#         while new_s < s:
#             s = new_s
#             new_s = apply(s, k)
#
#         return s


# Runtime: 32 ms, faster than 63.74% of Python3 online submissions for Orderly Queue.
# Memory Usage: 14.3 MB, less than 54.95% of Python3 online submissions for Orderly Queue.
# https://leetcode.com/problems/orderly-queue/solution/
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            c, result = Counter(s), ""
            return "".join([char * c[char] for char in sorted(c)])


tests = [
    [
        "cba", 1, "acb"
    ],
    [
        "baaca", 3, "aaabc"
    ],
    [
        "qasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnkqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducvnsdnvklsdjvnisdunvisuvnsdkjvsniduqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducvncvnvnvklsdjvnisdunvisuvnsdkjvsniducvnqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducvnqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducvnqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducvnqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducvnqasplregjiondfbviunsackjnreivnksvndlhkbsdkjcnkslacjnklsdjeriuvnksdnvklsdjvnisdunvisuvnsdkjvsniducvnrfijsokcs", 500, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffgggggggggghhhhhhhhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkllllllllllllllllllllllllllllllllllllllllllllllllllnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnoooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
    ],
    [
        "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffgggggggggghhhhhhhhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkllllllllllllllllllllllllllllllllllllllllllllllllllnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnoooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrruuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuussssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
        1,
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffgggggggggghhhhhhhhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkllllllllllllllllllllllllllllllllllllllllllllllllllnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnoooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrruuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuussssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
    ],
    [
        "fdcba",
        1,
        "afdcb"
    ]
]


run_functional_tests(Solution().orderlyQueue, tests)