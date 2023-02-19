"""
https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.



Example 1:

Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1
Explanation: source can be transformed the following way:
- Swap indices 0 and 1: source = [2,1,3,4]
- Swap indices 2 and 3: source = [2,1,4,3]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
Example 2:

Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
Output: 2
Explanation: There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
Example 3:

Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
Output: 0


Constraints:

n == source.length == target.length
1 <= n <= 105
1 <= source[i], target[i] <= 105
0 <= allowedSwaps.length <= 105
allowedSwaps[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""
from collections import defaultdict
from typing import List, Dict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1306 ms
# Beats
# 90.82%
# Memory
# 61.2 MB
# Beats
# 41.84%
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        def get_set_of_indices() -> Dict[int, List[int]]:
            n = len(source)
            p, rank = list(range(n)), [1] * n

            def get(i):
                while i != p[i]:
                    i = p[i]
                return i

            def connect(i, j):
                i = get(i)
                j = get(j)
                if rank[i] > rank[j]:
                    p[j] = i
                elif rank[j] > rank[i]:
                    p[i] = j
                else:
                    p[j] = i
                    rank[i] += 1

            for i, j in allowedSwaps:
                connect(i, j)

            result = defaultdict(list)
            for i in range(n):
                parent = get(i)
                result[parent].append(i)

            return result

        result = 0
        indices_groups = get_set_of_indices()
        for group in indices_groups:
            values = defaultdict(int)
            for i in indices_groups[group]:
                values[target[i]] += 1
            for i in indices_groups[group]:
                if source[i] not in values:
                    result += 1
                else:
                    values[source[i]] -= 1
                    if not values[source[i]]:
                        del values[source[i]]
        return result


tests = [
    [[50,46,54,35,18,42,26,72,75,47,50,4,54,21,18,18,61,64,100,14], [83,34,43,73,61,94,10,68,74,31,54,46,28,60,18,18,4,44,79,92], [[1,8],[14,17],[3,1],[17,10],[18,2],[7,12],[11,3],[1,15],[13,17],[18,19],[0,10],[15,19],[0,15],[6,7],[7,15],[19,4],[7,16],[14,18],[8,10],[17,0],[2,13],[14,10],[12,17],[2,9],[6,15],[16,18],[2,16],[2,6],[4,5],[17,5],[10,13],[7,2],[9,16],[15,5],[0,5],[8,0],[11,12],[9,7],[1,0],[11,17],[4,6],[5,7],[19,12],[3,18],[19,1],[13,18],[19,6],[13,6],[6,1],[4,2]], 14],
    [[1,2,3,4], [2,1,4,5], [[0,1],[2,3]], 1],
    [[1,2,3,4], [1,3,2,4], [], 2],
    [[5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]], 0],
]

run_functional_tests(Solution().minimumHammingDistance, tests)
