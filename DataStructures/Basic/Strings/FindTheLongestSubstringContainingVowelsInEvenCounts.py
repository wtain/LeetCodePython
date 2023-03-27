"""
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.



Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# WRONG & OVERCOMPLICATED
# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         counts = {v: 0 for v in vowels}
#         evens = {v: -1 for v in vowels}
#         odds = {v: math.inf for v in vowels}
#         result = 0
#         n = len(s)
#         for i in range(n):
#             l = i + 1
#             if s[i] in vowels:
#                 counts[s[i]] ^= 1
#                 if counts[s[i]]:
#                     l = i - odds[s[i]]
#                     if i < odds[s[i]]:
#                         odds[s[i]] = i
#                 else:
#                     l = i - evens[s[i]]
#                     if i < evens[s[i]]:
#                         evens[s[i]] = i
#             for v in vowels:
#                 if v == s[i]:
#                     continue
#                 if counts[v]:
#                     l1 = i - odds[v]
#                 else:
#                     l1 = i - evens[v]
#                 l = min(l, l1)
#             result = max(result, l)
#         return result

# WRONG
# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         counts = {v: 0 for v in vowels}
#         first = {v: math.inf for v in vowels}
#         result = 0
#         n = len(s)
#         for i in range(n):
#             l = i + 1
#             if s[i] in vowels:
#                 counts[s[i]] ^= 1
#                 if counts[s[i]]:
#                     l = i - first[s[i]] + 1
#                     if i < first[s[i]]:
#                         first[s[i]] = i
#                 else:
#                     l = i
#             for v in vowels:
#                 if v == s[i]:
#                     continue
#                 if counts[v]:
#                     l1 = i - first[v] + 1
#                 else:
#                     l1 = i
#                 l = min(l, l1)
#             result = max(result, l)
#         return result

# Runtime
# 737 ms
# Beats
# 35.60%
# Memory
# 20.3 MB
# Beats
# 9.85%
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        counts = [0] * n
        mask = 0
        prev_masks = [math.inf] * 32
        result = 0
        prev_masks[0] = -1
        for i in range(n):
            if s[i] == 'a':
                mask ^= 1
            elif s[i] == 'e':
                mask ^= 2
            elif s[i] == 'i':
                mask ^= 4
            elif s[i] == 'o':
                mask ^= 8
            elif s[i] == 'u':
                mask ^= 16
            length = i - prev_masks[mask]
            if prev_masks[mask] > i:
                prev_masks[mask] = i
            counts[i] = mask
            result = max(result, length)
        return result


tests = [
    ["eleetminicoworoep", 13],
    ["leetcodeisgreat", 5],
    ["bcbcbc", 6],
    ["tyrwpvlifrgjghlcicyocusukhmjbkfkzsjhkdrtsztchhazhmcircxcauajyzlppedqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz", 831],
]

run_functional_tests(Solution().findTheLongestSubstring, tests)
