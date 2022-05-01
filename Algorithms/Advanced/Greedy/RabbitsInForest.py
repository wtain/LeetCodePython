"""
https://leetcode.com/problems/rabbits-in-forest/

There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.



Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11


Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numRabbits(self, answers: List[int]) -> int:
#         d = defaultdict(int)
#         result = 0
#         for a in answers:
#             if not a:
#                 result += 1
#             else:
#                 d[a] += 1
#         for key in d:
#             result += max(key+1, d[key])
#         return result


# Runtime: 120 ms, faster than 5.10% of Python3 online submissions for Rabbits in Forest.
# Memory Usage: 13.9 MB, less than 97.77% of Python3 online submissions for Rabbits in Forest.
# https://leetcode.com/problems/rabbits-in-forest/discuss/1993399/Java-or-Hashmap-or-Easy-to-understand-or-No-mathematics-or-Simple-logic
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}
        result = 0
        for a in answers:
            if not a:
                result += 1
            elif a not in d:
                d[a] = a
                result += a+1
            else:
                d[a] -= 1
                if not d[a]:
                    del d[a]
        return result


tests = [
    [[1,1,2], 5],
    [[10,10,10], 11],
    [[1,1,2, 5], 11],
    [[0,0,1,1,1], 6]
]

run_functional_tests(Solution().numRabbits, tests)
