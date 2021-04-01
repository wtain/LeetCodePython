"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3687/
https://leetcode.com/problems/reconstruct-original-digits-from-english/

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 76.16% of Python3 online submissions for Reconstruct Original Digits from English.
# Memory Usage: 14.7 MB, less than 45.93% of Python3 online submissions for Reconstruct Original Digits from English.
# class Solution:
#     def originalDigits(self, s: str) -> str:
#         num_strs = [
#             "zero", "one", "two", "three", "four",
#             "five", "six", "seven", "eight", "nine"
#         ]
#         counters = [
#             Counter(s) for s in num_strs
#         ]
#         # z - 0
#         # w - 2
#         # u - 4
#         # x - 6
#         # g - 8
#         # "one", "three",
#         # "five", "seven", "nine"
#         # t - 3
#         # f - 5
#         # "one",
#         # "seven", "nine"
#         # v - 7
#         # "one",
#         # "nine"
#         # i - 9
#         ## counts = [Counter(ns) for ns in num_strs]
#         # lets = [for i in [chr(c) for c in range(ord('a'), ord('a')+26)]]
#         # lets = {}
#         # for i, c in enumerate(counts):
#         #     for ch in c.keys():
#         #         lets[ch] = lets.get(ch, []).append()  + c.get(ch)
#         c = Counter(s)
#         cnts = [0] * 10
#         cnts[0] = c['z']
#         cnts[2] = c['w']
#         cnts[4] = c['u']
#         cnts[6] = c['x']
#         cnts[8] = c['g']
#         for d in [0, 2, 4, 6, 8]:
#             for ch in counters[d].keys():
#                 c[ch] -= cnts[d] * counters[d][ch]
#         cnts[3] = c['t']
#         cnts[5] = c['f']
#         for d in [3, 5]:
#             for ch in counters[d].keys():
#                 c[ch] -= cnts[d] * counters[d][ch]
#         cnts[7] = c['v']
#         for d in [7]:
#             for ch in counters[d].keys():
#                 c[ch] -= cnts[d] * counters[d][ch]
#         cnts[9] = c['i']
#         for d in [9]:
#             for ch in counters[d].keys():
#                 c[ch] -= cnts[d] * counters[d][ch]
#         cnts[1] = c['o']
#         for d in [1]:
#             for ch in counters[d].keys():
#                 c[ch] -= cnts[d] * counters[d][ch]
#         result = ""
#         for i in range(10):
#             result += str(i) * cnts[i]
#         return result


# Runtime: 44 ms, faster than 87.21% of Python3 online submissions for Reconstruct Original Digits from English.
# Memory Usage: 14.6 MB, less than 66.28% of Python3 online submissions for Reconstruct Original Digits from English.
class Solution:
    def originalDigits(self, s: str) -> str:
        num_strs = [
            "zero", "two", "four", "six", "eight", "three", "five", "seven", "nine", "one"
        ]
        chars = [
            'z', 'w', 'u', 'x', 'g', 't', 'f', 'v', 'i', 'o'
        ]
        numbers = [
            0, 2, 4, 6, 8, 3, 5, 7, 9, 1
        ]
        counters = [
            Counter(s) for s in num_strs
        ]
        c = Counter(s)
        cnt = [0] * 10
        for i in range(10):
            count = c[chars[i]]
            cnt[numbers[i]] = count
            for ch in counters[i].keys():
                c[ch] -= counters[i][ch] * count
        result = ""
        for i in range(10):
            result += str(i) * cnt[i]
        return result


tests = [
    ("owoztneoer", "012"),
    ("fviefuro", "45")
]

run_functional_tests(Solution().originalDigits, tests)