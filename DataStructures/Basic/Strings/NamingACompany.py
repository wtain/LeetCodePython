"""
https://leetcode.com/problems/naming-a-company/description/

You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.



Example 1:

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.


Constraints:

2 <= ideas.length <= 5 * 104
1 <= ideas[i].length <= 10
ideas[i] consists of lowercase English letters.
All the strings in ideas are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def distinctNames(self, ideas: List[str]) -> int:
#         initial = set(ideas)
#         n = len(ideas)
#         result = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 idea1 = ideas[j][0] + ideas[i][1:]
#                 idea2 = ideas[i][0] + ideas[j][1:]
#                 if idea1 in initial:
#                     continue
#                 if idea2 in initial:
#                     continue
#                 result += 1
#                 if ideas[j][0] != ideas[i][0]:
#                     result += 1
#         return result


# TLE
# class Solution:
#     def distinctNames(self, ideas: List[str]) -> int:
#
#         M = 256
#
#         def word_hash(w: str) -> int:
#             nonlocal M
#             result = 0
#             for c in w[::-1]:
#                 result *= M
#                 result += ord(c)
#             return result
#
#         def change_hash(h: int, c: str) -> int:
#             nonlocal M
#             h //= M
#             h *= M
#             h += ord(c)
#             return h
#
#         ideas_s = set(ideas)
#         initial_hashes = [word_hash(word) for word in ideas]
#         initial = set(initial_hashes)
#         n = len(initial_hashes)
#         result = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 idea1 = change_hash(initial_hashes[i], ideas[j][0])
#                 idea2 = change_hash(initial_hashes[j], ideas[i][0])
#                 if idea1 in initial and (ideas[j][0] + ideas[i][1:]) in ideas_s:
#                     continue
#                 if idea2 in initial and (ideas[i][0] + ideas[j][1:]) in ideas_s:
#                     continue
#                 result += 1
#                 if ideas[j][0] != ideas[i][0]:
#                     result += 1
#         return result


# Runtime
# 592 ms
# Beats
# 83.69%
# Memory
# 28.8 MB
# Beats
# 28.26%
# https://leetcode.com/problems/naming-a-company/solutions/3081799/naming-a-company/
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        initial_groups = [set() for _ in range(256)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])

        result = 0
        for i in range(25):
            for j in range(i+1, 26):
                num_mutual = len(initial_groups[i] & initial_groups[j])
                result += 2 * (len(initial_groups[i]) - num_mutual) * (len(initial_groups[j]) - num_mutual)
        return result


tests = [
    [["coffee","donuts","time","toffee"], 6],
    [["lack","back"], 0],
]

run_functional_tests(Solution().distinctNames, tests)
