"""
https://leetcode.com/problems/hand-of-straights/

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.



Constraints:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""
from collections import Counter
from typing import List


# Runtime: 180 ms, faster than 81.57% of Python3 online submissions for Hand of Straights.
# Memory Usage: 15.9 MB, less than 26.00% of Python3 online submissions for Hand of Straights.
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W:
            return False
        m = n // W

        c = Counter(hand)
        nums_sorted = sorted(c.keys())
        ni = 0

        for i in range(m):
            prev = None
            for _ in range(W):
                if prev is not None:
                    if not c[prev + 1]:
                        return False
                    c[prev + 1] -= 1
                    prev += 1
                else:
                    while ni < len(nums_sorted) and not c[nums_sorted[ni]]:
                        ni += 1
                    if ni == len(nums_sorted):
                        return False
                    prev = nums_sorted[ni]
                    c[prev] -= 1
                    if not c[prev]:
                        ni += 1
        return True


tests = [
    ([0,0], 2, False),

    ([1,2,3,6,2,3,4,7,8], 3, True),
    ([1,2,3,4,5], 4, False)
]

for test in tests:
    result = Solution().isNStraightHand(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))