"""
https://leetcode.com/problems/smallest-sufficient-team/

In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.



Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]


Constraints:

1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] consists of lowercase English letters.
All the strings of req_skills are unique.
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] consists of lowercase English letters.
All the strings of people[i] are unique.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
#         skill_ids = {}
#         for i, skill in enumerate(req_skills):
#             skill_ids[skill] = i
#         all_skills_mask = (1 << len(req_skills)) - 1
#         people_masks = [0] * len(people)
#         for i, person in enumerate(people):
#             mask = 0
#             for skill in person:
#                 if skill not in skill_ids:
#                     continue
#                 mask += (1 << skill_ids[skill])
#             people_masks[i] = mask
#
#         return []


# Runtime
# Details
# 2901ms
# Beats 5.70%of users with Python3
# Memory
# Details
# 18.84mb
# Beats 60.13%of users with Python3
# https://leetcode.com/problems/smallest-sufficient-team/editorial/
# class Solution:
#     def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
#         skill_ids = {}
#         for i, skill in enumerate(req_skills):
#             skill_ids[skill] = i
#         people_masks = [0] * len(people)
#         for i, person in enumerate(people):
#             mask = 0
#             for skill in person:
#                 if skill not in skill_ids:
#                     continue
#                 mask += (1 << skill_ids[skill])
#             people_masks[i] = mask
#         n, m = len(people), len(req_skills)
#         dp = [(1 << n) - 1] * (1 << m)
#         dp[0] = 0
#         for skills_mask in range(1, 1 << m):
#             for i in range(n):
#                 smaller_skills_mask = skills_mask & ~people_masks[i]
#                 if smaller_skills_mask != skills_mask:
#                     pmask = dp[smaller_skills_mask] | (1 << i)
#                     if bin(pmask).count("1") < bin(dp[skills_mask]).count("1"):
#                         dp[skills_mask] = pmask
#
#         result_mask = dp[(1 << m) - 1]
#         result = []
#         for i in range(n):
#             if (result_mask >> i) & 1:
#                 result.append(i)
#         return result


# Runtime
# Details
# 994ms
# Beats 22.15%of users with Python3
# Memory
# Details
# 19.06mb
# Beats 57.60%of users with Python3
# https://leetcode.com/problems/smallest-sufficient-team/editorial/
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_ids = {}
        for i, skill in enumerate(req_skills):
            skill_ids[skill] = i
        people_masks = [0] * len(people)
        for i, person in enumerate(people):
            mask = 0
            for skill in person:
                if skill not in skill_ids:
                    continue
                mask += (1 << skill_ids[skill])
            people_masks[i] = mask
        n, m = len(people), len(req_skills)

        dp = [-1] * (1 << m)
        dp[0] = 0

        def f(skills_mask):
            if dp[skills_mask] != -1:
                return dp[skills_mask]
            for i in range(n):
                new_skills_mask = skills_mask & ~people_masks[i]
                if new_skills_mask != skills_mask:
                    pmask = f(new_skills_mask) | (1 << i)
                    if dp[skills_mask] == -1 or bin(pmask).count("1") < bin(dp[skills_mask]).count("1"):
                        dp[skills_mask] = pmask
            return dp[skills_mask]

        result_mask = f((1 << m) - 1)
        result = []
        for i in range(n):
            if (result_mask >> i) & 1:
                result.append(i)
        return result


tests = [
    [["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]], [0,2]],
    [["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]], [1,2]],
]

run_functional_tests(Solution().smallestSufficientTeam, tests)
