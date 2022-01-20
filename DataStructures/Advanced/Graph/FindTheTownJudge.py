"""
https://leetcode.com/problems/find-the-town-judge/

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1


Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1108 ms, faster than 8.72% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 19 MB, less than 23.32% of Python3 online submissions for Find the Town Judge.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t1, t2 = [0] * n, [0] * n
        for a, b in trust:
            t1[a-1] += 1
            t2[b-1] += 1
        result = -1
        for i in range(n):
            if not t1[i] and t2[i] == n-1:
                if result != -1:
                    return -1
                result = i + 1
        return result


tests = [
    [2, [[1,2]], 2],
    [3, [[1,3],[2,3]], 3],
    [3, [[1,3],[2,3],[3,1]], -1]
]

run_functional_tests(Solution().findJudge, tests)
