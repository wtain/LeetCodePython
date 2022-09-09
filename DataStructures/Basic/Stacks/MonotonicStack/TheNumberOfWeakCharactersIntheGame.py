"""
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.


Sort the array on the basis of the attack values and group characters with the same attack together. How can you use these groups?

Characters in one group will always have a lesser attack value than the characters of the next group. Hence, we will only need to check if there is a higher defense value present in the next groups.


Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.


Constraints:

2 <= properties.length <= 105
properties[i].length == 2
1 <= attacki, defensei <= 105
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 5264 ms, faster than 5.04% of Python3 online submissions for The Number of Weak Characters in the Game.
# Memory Usage: 66.8 MB, less than 89.75% of Python3 online submissions for The Number of Weak Characters in the Game.
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/2553781/Java-Sorting-O(n)
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda character: (-character[0], character[1]))
        number_of_weak = 0
        n = 0
        for attack, defense in properties:
            if defense < n:
                number_of_weak += 1
            n = max(n, defense)
        return number_of_weak


tests = [
    [[[5,5],[6,3],[3,6]], 0],
    [[[2,2],[3,3]], 1],
    [[[1,5],[10,4],[4,3]], 1]
]

run_functional_tests(Solution().numberOfWeakCharacters, tests)
