"""
https://leetcode.com/problems/best-poker-hand/

You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

"Flush": Five cards of the same suit.
"Three of a Kind": Three cards of the same rank.
"Pair": Two cards of the same rank.
"High Card": Any single card.
Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive.



Example 1:

Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
Output: "Flush"
Explanation: The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".
Example 2:

Input: ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
Output: "Three of a Kind"
Explanation: The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a "Three of a Kind".
Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
Also note that other cards could be used to make the "Three of a Kind" hand.
Example 3:

Input: ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
Output: "Pair"
Explanation: The hand with the first and second card consists of 2 cards with the same rank, so we have a "Pair".
Note that we cannot make a "Flush" or a "Three of a Kind".


Constraints:

ranks.length == suits.length == 5
1 <= ranks[i] <= 13
'a' <= suits[i] <= 'd'
No two cards have the same rank and suit.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 57 ms
# Beats
# 52.7%
# Memory
# 14 MB
# Beats
# 16.76%
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        def isFlush():
            return all(p == suits[0] for p in suits[1:])

        def isThreeOfAKind():
            return max(Counter(ranks).values()) >= 3

        def isPair():
            return max(Counter(ranks).values()) >= 2

        if isFlush():
            return "Flush"

        if isThreeOfAKind():
            return "Three of a Kind"

        if isPair():
            return "Pair"

        return "High Card"


tests = [
    [[13,2,3,1,9], ["a","a","a","a","a"], "Flush"],
    [[4,4,2,4,4], ["d","a","a","b","c"], "Three of a Kind"],
    [[10,10,2,12,9], ["a","b","c","a","d"], "Pair"]
]

run_functional_tests(Solution().bestHand, tests)
