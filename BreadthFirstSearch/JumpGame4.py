"""
https://leetcode.com/problems/jump-game-iv/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3582/
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3


Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8

Runtime: 588 ms, faster than 46.55% of Python3 online submissions for Jump Game IV.
Memory Usage: 27.3 MB, less than 91.59% of Python3 online submissions for Jump Game IV.
"""
from typing import List, Dict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # mat = [[0] * n for i in range(n)]
        # for i in range(n):
        #     if i+1 < n:
        #         mat[i][i+1] = 1
        #     if i-1 >= 0:
        #         mat[i][i-1] = 1
        valToIdx: Dict[int, List[int]] = {}
        for i in range(n):
            idx = valToIdx.get(arr[i], [])
            idx.append(i)
            valToIdx[arr[i]] = idx
        # for i in range(n):
        #     edges = valToIdx.get(arr[i], [])
        #     for j in edges:
        #         if i == j:
        #             continue
        #         mat[i][j] = 1
        #         mat[j][i] = 1
        # mat2 = [[n*n] * n for i in range(n)]
        visited = [False] * n
        toVisit = [0]
        step = 0
        while len(toVisit) > 0:
            nex = []
            for i in toVisit:
                if i == n-1:
                    return step
                edges = valToIdx.get(arr[i])
                if i-1 >= 0:
                    edges.append(i-1)
                if i+1 < n:
                    edges.append(i+1)
                for j in edges:
                    if not visited[j]:
                        visited[j] = True
                        nex.append(j)
                edges.clear()
            toVisit = nex
            step += 1
        return 0


tests = [
    ([100,-23,-23,404,100,23,23,23,3,404], 3),
    ([7], 0),
    ([7,6,9,6,9,6,9,7], 1),
    ([6,1,9], 2),
    ([11,22,7,7,7,7,7,7,7,22,13], 3)
]

for test in tests:
    result = Solution().minJumps(test[0])
    expected = test[1]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected), ", got " + str(result))