"""
https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Example 4:


Input: adjList = [[2],[1]]
Output: [[2],[1]]


Constraints:

1 <= Node.val <= 100
Node.val is unique for each node.
Number of Nodes will not exceed 100.
There is no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

Runtime: 68 ms, faster than 5.45% of Python3 online submissions for Clone Graph.
Memory Usage: 14.9 MB, less than 23.72% of Python3 online submissions for Clone Graph.

Runtime: 64 ms, faster than 5.45% of Python3 online submissions for Clone Graph.
Memory Usage: 14.6 MB, less than 48.96% of Python3 online submissions for Clone Graph.
"""

# Definition for a Node.
from typing import List, Dict


# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return None
#         toVisit = []
#         visited = []
#         cloned: Dict[Node, Node] = {}
#         toVisit.append(node)
#         cloned[node] = Node(node.val, [])
#         while len(toVisit) > 0:
#             n = toVisit.pop()
#             visited.append(n.val)
#             for a in n.neighbors:
#                 if a.val not in visited and a not in toVisit:
#                     toVisit.append(a)
#                     cloned[a] = Node(a.val, [])
#                 cloned[n].neighbors.append(cloned[a])
#         return cloned[node]


# Runtime: 40 ms, faster than 83.75% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.3 MB, less than 91.72% of Python3 online submissions for Clone Graph.
from Common.DataTypes.Graph import Node, buildGraph, getGraphAdj
from Common.Helpers.TestParamsHelpers import convert_test_params
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        cloned = {}

        def clone(node: Node) -> Node:
            if node.val in cloned:
                return cloned[node.val]
            copy = Node(node.val)
            cloned[node.val] = copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy

        if node is None:
            return None
        return clone(node)


tests = [
    [[[2,4],[1,3],[2,4],[1,3]], [[2, 4], [1, 3], [2, 4], [1, 3]]],
    [[[]], [[]]],
    [[], []],
    [[[2],[1]], [[2], [1]]]
]


run_functional_tests(Solution().cloneGraph, convert_test_params(tests, buildGraph))

