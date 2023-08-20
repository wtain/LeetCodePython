"""
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/

There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.



Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.


Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 332ms
# Beats 100.00%of users with Python3
# Memory
# Details
# 36.18MB
# Beats 64.41%of users with Python3
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/editorial/
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topological_sort(graph, indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for neib in graph[cur]:
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        stack.append(neib)
            return visited if len(visited) == len(graph) else []

        item_order = topological_sort(item_graph, item_indegree)
        group_order = topological_sort(group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        ordered_groups = defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        result = []
        for group_index in group_order:
            result += ordered_groups[group_index]

        return result


def customCheck(test, result) -> bool:
    n, m, group, before_items, expected = test
    if not result:
        return result == expected
    seen = set()
    for item in result:
        for before in before_items[item]:
            if before not in seen:
                return False
        seen.add(item)
    return True


tests = [
    [8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]], [6,3,4,1,5,2,0,7]],
    [8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]], []],
]

run_functional_tests(Solution().sortItems, tests, custom_check=customCheck)
