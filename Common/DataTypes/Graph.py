from typing import List


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def buildGraph(adj: List[List[int]]) -> Node:
    n = len(adj)
    nodes: List[Node] = []
    for i in range(n):
        nodes.append(Node(i+1, []))
    for i, ai in enumerate(adj):
        for j in ai:
            nodes[i].neighbors.append(nodes[j-1])
    return nodes[0] if len(nodes) > 0 else None


def getGraphAdj(n: Node) -> List[List[int]]:
    adj: List[List[int]] = []
    toVisit = []
    visited = []
    if n:
        toVisit.append(n)
    while len(toVisit) > 0:
        n = toVisit.pop()
        visited.append(n.val)
        while len(adj) < n.val:
            adj.append([])
        for a in n.neighbors:
            adj[n.val - 1].append(a.val)
            if a.val in visited or a in toVisit:
                continue
            toVisit.append(a)
    return adj


def is_graph_node(v) -> bool:
    return type(v) is Node


def graph_size(node) -> int:
    visited = set()
    count = 0
    to_visit = set()
    if node:
        to_visit.add(node)
    while to_visit:
        node = to_visit.pop()
        count += 1
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited and neighbor not in to_visit:
                to_visit.add(neighbor)
    return count


def graphs_equal(n1, n2) -> bool:
    return getGraphAdj(n1) == getGraphAdj(n2)
