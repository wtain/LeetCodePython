"""
https://leetcode.com/problems/pyramid-transition-matrix/

You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.



Example 1:


Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
Output: true
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
Example 2:


Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
Output: false
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.


Constraints:

2 <= bottom.length <= 6
0 <= allowed.length <= 216
allowed[i].length == 3
The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
All the values of allowed are unique.
"""
from collections import defaultdict
from functools import lru_cache, cache
from typing import List, Dict, Set

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
#
#         def build_dictionary(allowed: List[str]) -> Dict[str, Set[str]]:
#             dictionary = defaultdict(set)
#             for string in allowed:
#                 code = string[:2]
#                 letter = string[2:]
#                 dictionary[code].add(letter)
#             return dictionary
#
#         dictionary = build_dictionary(allowed)
#
#         def get_next_states(state: str, dictionary: Dict[str, Set[str]]) -> List[str]:
#             states = [""]
#             n = len(state)
#             for i in range(n-1):
#                 code = state[i:i+2]
#                 allowed = dictionary[code]
#                 new_states = []
#                 for next_state in states:
#                     for character in allowed:
#                         new_states.append(next_state + character)
#                 states = new_states
#
#             return states
#
#         to_visit = [bottom]
#         while to_visit:
#             state = to_visit.pop()
#             if state == "":
#                 return True
#             next_states = get_next_states(state, dictionary)
#             to_visit += next_states
#
#         return False


# Runtime
# 5731 ms
# Beats
# 15.89%
# Memory
# 25.1 MB
# Beats
# 15.89%
# class Solution:
#     def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
#
#         def build_dictionary(allowed: List[str]) -> Dict[str, Set[str]]:
#             dictionary = defaultdict(set)
#             for string in allowed:
#                 code = string[:2]
#                 letter = string[2:]
#                 dictionary[code].add(letter)
#             return dictionary
#
#         dictionary = build_dictionary(allowed)
#
#         @lru_cache(None)
#         def get_next_states(state: str) -> List[str]:
#             nonlocal dictionary
#             states = [""]
#             n = len(state)
#             for i in range(n-1):
#                 code = state[i:i+2]
#                 allowed = dictionary[code]
#                 new_states = []
#                 for next_state in states:
#                     for character in allowed:
#                         new_states.append(next_state + character)
#                 states = new_states
#
#             return states
#
#         to_visit = [bottom]
#         while to_visit:
#             state = to_visit.pop()
#             if state == "":
#                 return True
#             next_states = get_next_states(state)
#             to_visit += next_states
#
#         return False


# Runtime
# 754 ms
# Beats
# 60.92%
# Memory
# 196.1 MB
# Beats
# 6.62%
# https://leetcode.com/problems/pyramid-transition-matrix/solutions/2268424/python-3-bfs-and-dfs/
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        transitions = defaultdict(list)
        for string in allowed:
            transitions[string[:2]].append(string[2])

        @cache
        def dfs(state, index, next):
            nonlocal transitions
            if len(state) == 1:
                return True
            if len(state)-1 == len(next):
                return dfs(next, 0, "")
            if index == len(state) - 1:
                return False
            for char in transitions[state[index:index+2]]:
                if dfs(state, index+1, next+char):
                    return True
            return False

        return dfs(bottom, 0, "")


tests = [
    ["BCD", ["BCC","CDE","CEA","FFF"], True],
    ["AAAA", ["AAB","AAC","BCD","BBE","DEF"], False],

    ["ABBBBA", ["ACA","ACF","ACE","ACD","ABA","ABF","ABE","ABD","FCA","FCF","FCE","FCD","FBA","FBF","FBE","FBD","ECA","ECF","ECE","ECD","EBA","EBF","EBE","EBD","DCA","DCF","DCE","DCD","DBA","DBF","DBE","DBD","CAA","CAF","CAE","CAD","CFA","CFF","CFE","CFD","CEA","CEF","CEE","CED","CDA","CDF","CDE","CDD","BAA","BAF","BAE","BAD","BFA","BFF","BFE","BFD","BEA","BEF","BEE","BED","BDA","BDF","BDE","BDD","CCA","CCF","CCE","CCD","CBA","CBF","CBE","CBD","BCA","BCF","BCE","BCD","BBA","BBF","BBE","BBD","CCC","CCB","CBC","CBB","BCC","BCB","BBC","BBB"], False]
]

run_functional_tests(Solution().pyramidTransition, tests)
