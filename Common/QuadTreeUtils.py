from typing import List

from Common.Constants import null
from Common.DataTypes.QuadTree import Node


def build_quad_tree_from_list(values: List[List[int]]) -> Node:
    n = len(values)
    if not n:
        return null
    root = createNode(values[0])
    level = [root]
    i = 1
    while i < n:
        next_level = []
        for node in level:
            if i >= n:
                break
            if values[i] is not None:
                node.topLeft = createNode(values[i])
                next_level.append(node.topLeft)
            i += 1

            if i >= n:
                break
            if values[i] is not None:
                node.topRight = createNode(values[i])
                next_level.append(node.topRight)
            i += 1

            if i >= n:
                break
            if values[i] is not None:
                node.bottomLeft = createNode(values[i])
                next_level.append(node.bottomLeft)
            i += 1

            if i >= n:
                break
            if values[i] is not None:
                node.bottomRight = createNode(values[i])
                next_level.append(node.bottomRight)
            i += 1
        level = next_level
    return root


def createNode(value):
    isLeaf, val = value
    root = Node(val == 1, isLeaf == 1, None, None, None, None)
    return root


def printQuadTree(root: Node):
    visited = set()

    def printTreeImpl(root: Node):
        nonlocal visited
        if root is None:
            return
        if root in visited:
            print("*** Loop detected -> Aborting")
            return
        visited.add(root)
        if root.isLeaf:
            print(root.val)
        print('(', end='')
        printTreeImpl(root.topLeft)
        print(",", end='')
        printTreeImpl(root.topRight)
        print(')', end='')
        printTreeImpl(root.bottomLeft)
        print(",", end='')
        printTreeImpl(root.bottomRight)
        print(')', end='')

    printTreeImpl(root)
    print()


def compareQuadTrees(t1: Node, t2: Node) -> bool:
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return compareQuadTrees(t1.topLeft, t2.topLeft) and \
           compareQuadTrees(t1.topRight, t2.topRight) and \
           compareQuadTrees(t1.bottomLeft, t2.bottomLeft) and \
           compareQuadTrees(t1.bottomRight, t2.bottomRight)
