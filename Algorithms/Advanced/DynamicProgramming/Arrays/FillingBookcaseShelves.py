"""
https://leetcode.com/problems/filling-bookcase-shelves/

You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.



Example 1:


Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
Example 2:

Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4


Constraints:

1 <= books.length <= 1000
1 <= thicknessi <= shelfWidth <= 1000
1 <= heighti <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 51 ms
# Beats
# 71.86%
# Memory
# 14.1 MB
# Beats
# 99.33%
# https://leetcode.com/problems/filling-bookcase-shelves/solutions/323315/java-dp-solution/
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            w, h = books[i-1]
            dp[i] = dp[i-1] + h
            for j in range(i-1, 0, -1):
                if w + books[j-1][0] > shelfWidth:
                    break
                h = max(h, books[j-1][1])
                w += books[j-1][0]
                dp[i] = min(dp[i], dp[j-1] + h)
        return dp[-1]

"""

H(0) = 0
W(0) = 0

H(1) = h1
W(1) = w1

H(n) = min(max(H(n-1), hn), H(n-1)+hn) if H(n-1)+hn <=  shelfWidth  else  H(n-1)+hn 
"""

tests = [
    [[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4, 6],
    [[[1,3],[2,4],[3,2]], 6, 4],
]

run_functional_tests(Solution().minHeightShelves, tests)
