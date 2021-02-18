"""
https://leetcode.com/problems/positions-of-large-groups/
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.



Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".
Example 4:

Input: s = "aba"
Output: []


Constraints:

1 <= s.length <= 1000
s contains lower-case English letters only.

Runtime: 40 ms, faster than 50.69% of Python3 online submissions for Positions of Large Groups.
Memory Usage: 14.4 MB, less than 18.66% of Python3 online submissions for Positions of Large Groups.
"""
from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        n = len(s)
        if n == 0:
            return result
        pos = 0
        def checkGroup(i: int):
            nonlocal pos
            if i-pos+1 >= 3:
                result.append([pos, i])
        for i in range(1, n+1):
            if i == n:
                checkGroup(i-1)
            elif s[i] != s[i-1]:
                checkGroup(i - 1)
                pos = i

        return result


def compareResults(result: List[List[int]], expected: List[List[int]]) -> bool:
    n1 = len(result)
    n2 = len(expected)
    if n1 != n2:
        return False
    for i in range(n1):
        if result[i][0] != expected[i][0] or result[i][1] != expected[i][1]:
            return False
    return True


tests = [
    ("abbxxxxzzy", [[3,6]]),
    ("abc", []),
    ("abcdddeeeeaabbbcd", [[3,5],[6,9],[12,14]]),
    ("aba", [])
]

for test in tests:
    result = Solution().largeGroupPositions(test[0])
    if compareResults(result, test[1]):
        print('PASS')
    else:
        print('FAIL')
