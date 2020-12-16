"""
https://leetcode.com/problems/shortest-distance-to-a-character/
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

Runtime: 64 ms, faster than 31.97% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.3 MB, less than 60.38% of Python3 online submissions for Shortest Distance to a Character.


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c: chr = C[0]
        n = len(S)
        result: List[int] = [n+1] * n
        prev = -1
        i = 0
        while i < n:
            j = S.find(c, i)
            if j == -1:
                j = n
            else:
                result[j] = 0
            for k in range(i, j):
                if j != n:
                    result[k] = min(result[k], j-k)
                if prev != -1:
                    result[k] = min(result[k], k - prev)
            prev = j
            i = j + 1
        return result

Runtime: 44 ms, faster than 43.17% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.5 MB, less than 11.93% of Python3 online submissions for Shortest Distance to a Character.
"""
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c: chr = C[0]
        n = len(S)
        result: List[int] = [n+1] * n
        prev = -1
        for i in range(n):
            if S[i] == c:
                result[i] = 0
                prev = i
            elif prev != -1:
                result[i] = i - prev

        prev = n
        for i in range(n-1, -1, -1):
            if S[i] == c:
                result[i] = 0
                prev = i
            elif prev != n:
                result[i] = min(prev - i, result[i])

        return result


print(Solution().shortestToChar("abaa", 'b'))  # [1,0,1,2]
print(Solution().shortestToChar("loveleetcode", 'e'))  # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]