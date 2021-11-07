"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3887/
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
from collections import Counter, defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.ResultComparators import compareSets, compareSetsOfSets


# Runtime: 251 ms, faster than 5.01% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.3 MB, less than 77.16% of Python3 online submissions for Group Anagrams.
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         def hash(s: str) -> str:
#             c = Counter(s)
#             return "".join(ch + str(c[ch]) for ch in sorted(c.keys()))
#
#         buckets = defaultdict(list)
#
#         for s in strs:
#             buckets[hash(s)].append(s)
#
#         return [v for v in buckets.values()]


# Runtime: 259 ms, faster than 5.01% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.3 MB, less than 77.16% of Python3 online submissions for Group Anagrams.
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         def hash(s: str) -> int:
#             c = Counter(s)
#             return sum(26**(ord(ch)-ord('a')) * c[ch] for ch in c.keys())
#
#         buckets = defaultdict(list)
#
#         for s in strs:
#             buckets[hash(s)].append(s)
#
#         return [v for v in buckets.values()]


# Runtime: 190 ms, faster than 6.97% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.3 MB, less than 71.88% of Python3 online submissions for Group Anagrams.
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         def hash(s: str) -> int:
#             return sum(26**(ord(c)-ord('a')) for c in s)
#
#         buckets = defaultdict(list)
#
#         for s in strs:
#             buckets[hash(s)].append(s)
#
#         return [v for v in buckets.values()]


# Runtime: 192 ms, faster than 6.97% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.5 MB, less than 64.22% of Python3 online submissions for Group Anagrams.
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         def hash(s: str) -> int:
#             return sum(26**(ord(c)-ord('a')) for c in s)
#
#         buckets = defaultdict(list)
#
#         for s in strs:
#             buckets[hash(s)].append(s)
#
#         return buckets.values()


# Runtime: 189 ms, faster than 6.97% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.9 MB, less than 50.48% of Python3 online submissions for Group Anagrams.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def hash(s: str) -> int:
            return sum(1000**(ord(c)-ord('a')) for c in s)

        buckets = defaultdict(list)

        for s in strs:
            buckets[hash(s)].append(s)

        return buckets.values()


tests = [
    [["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]],
    [[""], [[""]]],
    [["a"], [["a"]]]
]

run_functional_tests(Solution().groupAnagrams, tests, custom_check=compareSetsOfSets)