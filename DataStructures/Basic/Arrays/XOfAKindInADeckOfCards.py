"""
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].


Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4

Runtime: 140 ms, faster than 28.28% of Python3 online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 14.6 MB, less than 30.96% of Python3 online submissions for X of a Kind in a Deck of Cards.
"""
from typing import List
from math import gcd
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def find_gcd(list):
            x = reduce(gcd, list)
            return x

        counts = {}
        for c in deck:
            counts[c] = counts.get(c, 0) + 1
        counts = counts.values()

        return find_gcd(counts) >= 2


tests = [
    ([1,1,1,1,2,2,2,2,2,2], True),

    ([1,2,3,4,4,3,2,1],True),
    ([1,1,1,2,2,2,3,3], False),
    ([1], False),
    ([1,1], True),
    ([1,1,2,2,2,2], True)
]

for test in tests:
    if Solution().hasGroupsSizeX(test[0]) != test[1]:
        print("FAIL")
    else:
        print("PASS")