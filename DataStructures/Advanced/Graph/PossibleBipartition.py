"""
https://leetcode.com/problems/possible-bipartition/
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Constraints:

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""
from typing import List


# Runtime: 724 ms, faster than 49.95% of Python3 online submissions for Possible Bipartition.
# Memory Usage: 19.8 MB, less than 66.30% of Python3 online submissions for Possible Bipartition.
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        def build_graph(N: int, dislikes: List[List[int]]) -> List[List[int]]:
            graph = [[] for _ in range(N)]
            for edge in dislikes:
                i, j = edge
                i -= 1
                j -= 1
                graph[i].append(j)
                graph[j].append(i)

            return graph

        graph = build_graph(N, dislikes)

        labels = [0] * N
        for i in range(N):
            if labels[i]:
                continue
            toVisit = [[i, 1]]
            while toVisit:
                j, label = toVisit.pop()
                if labels[j]:
                    if labels[j] != label:
                        return False
                    else:
                        continue
                labels[j] = label
                for k in graph[j]:
                    toVisit.append([k, 3 - label])
        return True


tests = [
    (4, [[1,2],[1,3],[2,4]], True),
    (3, [[1,2],[1,3],[2,3]], False),
    (5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False)
]

for test in tests:
    result = Solution().possibleBipartition(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))