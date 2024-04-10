"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/description/?envType=daily-question&envId=2024-04-10

You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

Note that the first entry in the answer is considered to be the top of the deck.



Example 1:

Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation:
We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
Example 2:

Input: deck = [1,1000]
Output: [1,1000]


Constraints:

1 <= deck.length <= 1000
1 <= deck[i] <= 106
All the values of deck are unique.
"""
from collections import deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 50
# ms
# Beats
# 28.88%
# of users with Python3
# Memory
# 16.89
# MB
# Beats
# 36.98%
# of users with Python3
# https://leetcode.com/problems/reveal-cards-in-increasing-order/editorial/?envType=daily-question&envId=2024-04-10
# class Solution:
#     def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
#         n = len(deck)
#         result = [0] * n
#         skip = False
#         index_in_deck = 0
#         index_in_result = 0
#         deck.sort()
#         while index_in_deck < n:
#             if result[index_in_result] == 0:
#                 if not skip:
#                     result[index_in_result] = deck[index_in_deck]
#                     index_in_deck += 1
#                 skip = not skip
#             index_in_result = (index_in_result + 1) % n
#         return result


# Runtime
# 47
# ms
# Beats
# 48.83%
# of users with Python3
# Memory
# 16.79
# MB
# Beats
# 80.95%
# of users with Python3
# https://leetcode.com/problems/reveal-cards-in-increasing-order/editorial/?envType=daily-question&envId=2024-04-10
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque()
        for i in range(n):
            q.append(i)
        deck.sort()
        result = [0] * n
        for card in deck:
            result[q.popleft()] = card
            if q:
                q.append(q.popleft())
        return result


tests = [
    [[17,13,11,2,3,5,7], [2,13,3,11,5,17,7]],
    [[1,1000], [1,1000]],
]

run_functional_tests(Solution().deckRevealedIncreasing, tests)
