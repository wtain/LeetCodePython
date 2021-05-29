"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3739/
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1.
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202


Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

Let the sum of all points be total_pts. You need to remove a sub-array from cardPoints with length n - k.

Keep a window of size n - k over the array. The answer is max(answer, total_pts - sumOfCurrentWindow)
"""
from typing import List


# Runtime: 432 ms, faster than 40.19% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
# Memory Usage: 27.6 MB, less than 31.77% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        score = 0
        for i in range(n-k):
            score += cardPoints[i]
        min_score = score
        i1, i2 = 0, n-k
        while i2 < n:
            score -= cardPoints[i1]
            score += cardPoints[i2]
            min_score = min(min_score, score)
            i1 += 1
            i2 += 1
        return sum(cardPoints) - min_score


tests = [
    [[1,2,3,4,5,6,1], 3, 12],
    [[2,2,2], 2, 4],
    [[9,7,7,9,7,7,9], 7, 55],
    [[1,1000,1], 1, 1],
    [[1,79,80,1,1,1,200,1], 3, 202]
]